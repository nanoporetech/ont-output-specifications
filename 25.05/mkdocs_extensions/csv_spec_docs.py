from markdown import Markdown
from markdown.extensions import Extension
from pathlib import Path
from xml.etree import ElementTree as etree
import re

import yaml

from doc_utils import (
    SpecProcessor,
    CommonFieldLoader,
    SequencingSummaryField,
    SampleSheetField,
)


class CsvDocProcessor(SpecProcessor):
    CLASSNAME = "autodoc"
    RE = re.compile(r"(?:^|\n):::\s+csv_spec_docs\s+(.*)(?:\n|$)")
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

        common_fields = CommonFieldLoader()

        if m:
            doc_name = m.group(1)

            autodoc_div = etree.SubElement(parent, "div")
            autodoc_div.set("class", self.CLASSNAME)

            self.render_csv_spec(autodoc_div, doc_name, common_fields)

    def render_csv_spec(
        self, parent: etree.Element, spec_name: str, common_fields: CommonFieldLoader
    ) -> None:
        if spec_name == "sequencing_summary":
            common_field_type = SequencingSummaryField
        elif spec_name == "sample_sheet":
            common_field_type = SampleSheetField
        else:
            raise ValueError(f"Unknown doc type: {spec_name}")

        doc_path = Path(f"{spec_name}/spec.yaml")
        if not doc_path.exists():
            raise ValueError(f"Path does not exist: {doc_path}")

        # Read the input file
        with open(doc_path, "r") as f:
            input_spec = yaml.load(f, Loader=yaml.FullLoader)

            header_type = "fastq"

            for header_item in input_spec["file"]["columns"]:
                level = 3
                field_content = self.add_field_heading(
                    parent, header_type, level, header_item["name"]
                )
                if "regex" in header_item:
                    self.add_key_value(
                        field_content, "Regex", header_item["regex"], code=True
                    )
                if "required" not in header_item or header_item["required"] is True:
                    self.add_required(field_content)
                if "only_when" in header_item:
                    self.add_key_value(
                        field_content, "Only When", header_item["only_when"], code=True
                    )

                common_item = common_fields.find_common_field(
                    common_field_type(header_item["name"])
                )
                if common_item:
                    self.add_common_section(field_content, common_item, spec_name)

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
        processor = CsvDocProcessor(md.parser, md=md)
        md.parser.blockprocessors.register(processor, "csv_spec_docs", 110)


def makeExtension():
    return MKAutoDocExtension()
