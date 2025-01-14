from markdown import Markdown
from markdown.extensions import Extension
from xml.etree import ElementTree as etree
import re

import yaml

from doc_utils import SpecProcessor


class BamDocProcessor(SpecProcessor):
    CLASSNAME = "autodoc"
    RE = re.compile(r"(?:^|\n):::\s+fastq_spec_docs\s+(header)(?:\n|$)")
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

            autodoc_div = etree.SubElement(parent, "div")
            autodoc_div.set("class", self.CLASSNAME)

            if doc_type == "header":
                self.render_fastq_header(autodoc_div)
            else:
                raise ValueError(f"Unknown doc type: {doc_type}")

    def render_fastq_header(self, parent: etree.Element) -> None:
        # Read the input file
        with open("fastq/header-spec.yaml", "r") as f:
            input_spec = yaml.load(f, Loader=yaml.FullLoader)

            header_type = "fastq"

            for header_item in input_spec["file"]["headers"]:
                level = 3
                field_content = self.add_field_heading(
                    parent, header_type, level, header_item["name"]
                )
                if "regex" in header_item:
                    self.add_key_value(
                        field_content, "Regex", header_item["regex"], code=True
                    )
                if header_item["required"]:
                    self.add_required(field_content)
                if "only_when" in header_item:
                    self.add_key_value(
                        field_content, "Only When", header_item["only_when"], code=True
                    )
                if "examples" in header_item:
                    self.add_table(
                        field_content,
                        [["Examples"]] + [[k] for k in header_item["examples"]],
                        code=True,
                    )
                self.add_field_content(field_content, header_item["description"])


class MKAutoDocExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        md.registerExtension(self)
        processor = BamDocProcessor(md.parser, md=md)
        md.parser.blockprocessors.register(processor, "fastq_spec_docs", 110)


def makeExtension():
    return MKAutoDocExtension()
