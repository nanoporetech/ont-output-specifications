from markdown import Markdown
from markdown.extensions import Extension
from xml.etree import ElementTree as etree
import re

import yaml

from doc_utils import SpecProcessor, CommonFieldLoader


class PatternDocProcessor(SpecProcessor):
    CLASSNAME = "autodoc"
    RE = re.compile(r"(?:^|\n):::\s+pattern_docs\s+(global|read)(?:\n|$)")
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

        CommonFieldLoader()

        if m:
            doc_type = m.group(1)

            autodoc_div = etree.SubElement(parent, "div")
            autodoc_div.set("class", self.CLASSNAME)

            # Read the input file
            with open("patterns.yaml", "r") as f:
                input_spec = yaml.load(f, Loader=yaml.FullLoader)

                for name, header_item in input_spec["patterns"].items():
                    if header_item["context"] != doc_type:
                        continue

                    level = 4
                    field_content = self.add_field_heading(
                        parent, "pattern", level, name
                    )
                    if "regex" in header_item:
                        self.add_key_value(
                            field_content, "Regex", header_item["regex"], code=True
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
        processor = PatternDocProcessor(md.parser, md=md)
        md.parser.blockprocessors.register(processor, "pattern_docs", 110)


def makeExtension():
    return MKAutoDocExtension()
