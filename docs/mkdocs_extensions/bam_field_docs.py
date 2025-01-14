from markdown import Markdown
from markdown.extensions import Extension
from xml.etree import ElementTree as etree
import re

import yaml

from doc_utils import SpecProcessor


class BamDocProcessor(SpecProcessor):
    CLASSNAME = "autodoc"
    RE = re.compile(
        r"(?:^|\n):::\s+bam_spec_docs\s+(header_records|read_tags)\s*([A-Z]{2})?(?:\n|$)"
    )
    RE_SPACES = re.compile("  +")

    def __init__(self, parser, md=None):
        super().__init__(parser=parser)
        self.md = md

    def test(self, parent: etree.Element, block: etree.Element) -> bool:
        self.lastChild(parent)
        return bool(self.RE.search(block))

    def run(self, parent: etree.Element, blocks: etree.Element) -> None:
        self.lastChild(parent)
        block = blocks.pop(0)
        m = self.RE.search(block)

        if m:
            block = block[m.end() :]  # removes the first line

        block, theRest = self.detab(block)
        print(block)

        if m:
            doc_type = m.group(1)
            sub_type = m.group(2)

            autodoc_div = etree.SubElement(parent, "div")
            autodoc_div.set("class", self.CLASSNAME)

            if doc_type == "header_records":
                self.render_bam_headers(autodoc_div, sub_type)
            elif doc_type == "read_tags":
                self.render_bam_read_tags(autodoc_div)
            else:
                raise ValueError(f"Unknown doc type: {doc_type}")

    def render_bam_headers(self, parent: etree.Element, header_type: str) -> None:
        # Read the input file
        with open("bam/spec.yaml", "r") as f:
            input_spec = yaml.load(f, Loader=yaml.FullLoader)

            for header_item in input_spec["file"]["header_records"]:
                if header_item["type"] == header_type:
                    level = 4
                    field_content = self.add_field_heading(
                        parent, header_type, level, header_item["field"]
                    )
                    if "regex" in header_item:
                        self.add_key_value(
                            field_content, "Regex", header_item["regex"], code=True
                        )
                    if header_item["required"]:
                        self.add_required(field_content)
                    if "examples" in header_item:
                        self.add_table(
                            field_content,
                            [["Examples"]] + [[k] for k in header_item["examples"]],
                            code=True,
                        )
                    self.add_field_content(field_content, header_item["description"])

    def render_bam_read_tags(self, parent: etree.Element) -> None:
        # Read the input file
        with open("bam/spec.yaml", "r") as f:
            input_spec = yaml.load(f, Loader=yaml.FullLoader)

            level = 4
            field_type = "read_tags"

            for header_item in input_spec["file"]["read_tags"]:
                extra = f":{header_item['type']}:{header_item.get('value', '')}"
                field_content = self.add_field_heading(
                    parent, field_type, level, header_item["tag"], [extra]
                )
                if header_item.get("required", False):
                    self.add_required(field_content)
                if "only_when" in header_item:
                    self.add_key_value(
                        field_content, "Only When", header_item["only_when"], code=True
                    )
                self.add_field_content(field_content, header_item["description"])


class MKAutoDocExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        md.registerExtension(self)
        processor = BamDocProcessor(md.parser, md=md)
        md.parser.blockprocessors.register(processor, "bam_spec_docs", 110)


def makeExtension():
    return MKAutoDocExtension()
