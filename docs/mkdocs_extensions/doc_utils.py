from markdown import Markdown
from markdown.blockprocessors import BlockProcessor
from xml.etree import ElementTree as etree


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

    def add_key_value(self, parent: etree.Element, key, value, code=False):
        root = etree.SubElement(parent, "div")

        required_elem = etree.SubElement(root, "strong")
        required_elem.set("class", "doc-keyvalue")
        required_elem.text = f"{key} "

        if code:
            value_elem = etree.SubElement(root, "code")
        else:
            value_elem = etree.SubElement(root, "span")
        value_elem.text = value

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
