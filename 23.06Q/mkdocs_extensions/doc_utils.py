from dataclasses import dataclass
import html
from typing import Any

from markdown import Markdown
from markdown.blockprocessors import BlockProcessor
from xml.etree import ElementTree as etree

import yaml


@dataclass
class BamField:
    area: str
    field: str


@dataclass
class FastqField:
    field: str


@dataclass
class SampleSheetField:
    column: str


@dataclass
class SequencingSummaryField:
    column: str


@dataclass
class CommonField:
    fields: dict[str, Any]

    def build(self, parent: etree.Element, without: str = None):
        NICE_MAP = {
            "bam": "BAM",
            "fastq": "FASTQ",
            "sequencing_summary": "Sequencing summary",
            "sample_sheet": "Sample sheet",
        }
        for name, field in self.fields.items():
            if name == without:
                continue

            value_elem = etree.SubElement(parent, "code")
            value_elem.set("class", "doc-common-value")
            value_elem.text = f"{NICE_MAP[name]}: "

            if name == "bam":
                value_elem = etree.SubElement(value_elem, "span")
                value_elem.text = (
                    f"[{field['field']}](/read_formats/bam#{field['link'].lower()})"
                )
            elif name == "fastq":
                value_elem = etree.SubElement(value_elem, "span")
                value_elem.text = f"[{field}](/read_formats/fastq#{field.lower()})"
            elif name == "sample_sheet":
                value_elem = etree.SubElement(value_elem, "span")
                value_elem.text = (
                    f"[{field}](/protocol_formats/sample_sheet#{field.lower()})"
                )
            elif name == "sequencing_summary":
                value_elem = etree.SubElement(value_elem, "span")
                value_elem.text = (
                    f"[{field}](/protocol_formats/sequencing_summary#{field.lower()})"
                )


class CommonFieldLoader:
    def __init__(self):
        with open("./common_fields.yaml", "r") as f:
            self.common_fields = yaml.load(f, Loader=yaml.FullLoader)

    def find_common_field(
        self,
        source_file: BamField | FastqField | SampleSheetField | SequencingSummaryField,
    ) -> CommonField:
        """
        Find a common field for a given source file

        :param source_file: The source file to find a common field for
        """
        with open("./common_fields.yaml", "r") as f:
            common_fields = yaml.load(f, Loader=yaml.FullLoader)

            for name, value in common_fields["common_fields"].items():
                if isinstance(source_file, BamField):
                    if (
                        "bam" in value
                        and value["bam"]["area"] == source_file.area
                        and value["bam"]["field"] == source_file.field
                    ):
                        return CommonField(fields=value)
                elif isinstance(source_file, FastqField):
                    if "fastq" in value and value["fastq"] == source_file.field:
                        return CommonField(fields=value)
                elif isinstance(source_file, SampleSheetField):
                    if (
                        "sample_sheet" in value
                        and value["sample_sheet"] == source_file.column
                    ):
                        return CommonField(fields=value)
                elif isinstance(source_file, SequencingSummaryField):
                    if (
                        "sequencing_summary" in value
                        and value["sequencing_summary"] == source_file.column
                    ):
                        return CommonField(fields=value)

        return None


class SpecProcessor(BlockProcessor):
    def add_field_heading(
        self,
        parent: etree.Element,
        field_type: int,
        heading_level: int,
        name: str,
        extra: list[str] = None,
    ) -> etree.Element:
        # Eg: `some_module.attribute_name`
        signature_elem = etree.SubElement(parent, "div")
        signature_elem.set("class", "doc-signature")

        heading_elem = etree.SubElement(signature_elem, f"h{heading_level}")
        heading_elem.set("class", f"doc-fieldname_{field_type}")
        name_elem = etree.SubElement(heading_elem, "code")
        name_elem.text = name

        if extra:
            for extra_name in extra:
                qualifier_elem = etree.SubElement(heading_elem, "em")
                qualifier_elem.text = f"{extra_name} "

        content_elem = etree.SubElement(parent, "div")
        content_elem.set("class", "doc-docstring")

        return content_elem

    def add_field_content(self, parent: etree.Element, content: str):
        docstring_elem_content = etree.SubElement(parent, "div")

        md = Markdown(extensions=self.md.registeredExtensions)
        docstring_elem_content.text = md.convert(content)

    def add_required(self, parent: etree.Element):
        self.add_key_value(parent, "Required", "")

    def add_common_section(
        self, parent: etree.Element, common_item: CommonField, source_area: str
    ):
        root = etree.SubElement(parent, "div")

        required_elem = etree.SubElement(root, "strong")
        required_elem.set("class", "doc-keyvalue")
        required_elem.text = "Common fields "

        common_item.build(root, without=source_area)

    def add_key_value(self, parent: etree.Element, key, value, code=False):
        root = etree.SubElement(parent, "div")

        required_elem = etree.SubElement(root, "strong")
        required_elem.set("class", "doc-keyvalue")
        required_elem.text = f"{key} "

        if code:
            value_elem = etree.SubElement(root, "code")
        else:
            value_elem = etree.SubElement(root, "span")
        value_elem.text = self.html_escape_string(value)

    def add_table(self, parent: etree.Element, data: list[list[str]], code=False):
        root = etree.SubElement(parent, "div")

        table_elem = etree.SubElement(root, "table")

        def render_rows(parent, data, cell_type="td", code=False):
            for row in data:
                row_elem = etree.SubElement(parent, "tr")
                for cell in row:
                    cell_elem = etree.SubElement(row_elem, cell_type)
                    if code:
                        cell_elem = etree.SubElement(cell_elem, "code")
                        cell_elem.text = cell
                    else:
                        cell_elem.text = cell

        table_head = etree.SubElement(table_elem, "thead")
        render_rows(table_head, data[:1], "th")

        table_body = etree.SubElement(table_elem, "tbody")
        render_rows(table_body, data[1:], "td", code=code)

    def html_escape_string(self, string: str) -> str:
        escaped = html.escape(string)
        escaped = escaped.replace("\\", "&#92;")
        return escaped
