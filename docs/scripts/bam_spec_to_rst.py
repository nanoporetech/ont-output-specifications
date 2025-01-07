import argparse
import tabulate
import yaml

from rst_utils import RstWriter, HeadingLevels


def main():
    parser = argparse.ArgumentParser(description="Convert a BAM specification to RST")
    parser.add_argument(
        "input_file",
        type=argparse.FileType("r"),
        help="The input BAM specification file",
    )
    parser.add_argument(
        "output_file", type=argparse.FileType("w"), help="The output RST file"
    )
    args = parser.parse_args()

    # Read the input file
    with args.input_file as f:
        input_spec = yaml.load(f, Loader=yaml.FullLoader)

    writer = RstWriter()

    writer.title(level=HeadingLevels.H2, title="Specification")

    writer.file_version_label(input_spec["file"]["version"])

    read_group_table = []
    program_table = []
    for header_item in input_spec["file"]["header_records"]:
        table = read_group_table if header_item["type"] == "RG" else program_table
        table.append(header_item)

    def format_item(writer, item):
        writer.raw(f".. filefield:: {item['field']}")
        writer.raw(f"  :content: {item['content']}")

        if item["required"]:
            writer.raw("  :required:")

        if "regex" in read_group:
            writer.raw(f"  :regex: {item['regex']}")

        if "comments" in item:
            writer.raw("\n  " + item.get("comments", "").replace("\n", "\n  "))

        if "examples" in item:
            examples = "  **Examples:**\n\n  "
            examples += tabulate.tabulate(
                [[f"``{e}``"] for e in item["examples"]], tablefmt="grid"
            ).replace("\n", "\n  ")

            writer.raw(examples)

    writer.title(level=HeadingLevels.H3, title="Read Group")
    for read_group in read_group_table:
        format_item(writer, read_group)
    writer.raw("\n")

    writer.title(level=HeadingLevels.H3, title="Program Records")
    for program_item in program_table:
        format_item(writer, program_item)
    writer.raw("\n")

    writer.title(level=HeadingLevels.H3, title="Read Tags")

    for read_tag in input_spec["file"]["read_tags"]:
        writer.raw(f".. filefield:: {read_tag['tag']}")

        if "comment" in read_tag:
            writer.raw("\n  " + read_tag.get("comment", "").replace("\n", "\n  "))
    writer.write(args.output_file)


if __name__ == "__main__":
    main()
