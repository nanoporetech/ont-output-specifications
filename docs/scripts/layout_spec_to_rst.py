import argparse
from pathlib import Path
import yaml

from rst_utils import RstWriter, HeadingLevels


def generate_batching_section(writer, batching_spec):
    writer.title(level=HeadingLevels.H2, title="Read Batching")

    writer.text("The following batching options are used by default:\n")

    batching_options = []
    if "duration" in batching_spec:
        batching_options.append(["**Duration**", batching_spec["duration"]])
    if "bases" in batching_spec:
        batching_options.append(["**Bases**", batching_spec["bases"]])
    if "read_count" in batching_spec:
        batching_options.append(["**Read count**", batching_spec["read_count"]])

    writer.table(batching_options, headers=["Option", "Value"])


def generate_path_footer(writer):
    writer.text(
        "See the :doc:`../file_patterns` documentation "
        "for more information on file patterns."
    )


def generate_bam_paths(input_spec, output_file):
    writer = RstWriter()

    writer.title(level=HeadingLevels.H2, title="Paths")

    writer.text("The following path patterns are used by place reads:\n")

    path_table = [
        ["**Bam File**", f"``{input_spec['bam_path']}``"],
        ["**Bai File**", f"``{input_spec['bai_path']}``"],
    ]
    writer.table(path_table, headers=["File", "Path Pattern"])

    generate_path_footer(writer)

    generate_batching_section(writer, input_spec["batching"])

    writer.write(output_file)


def main():
    parser = argparse.ArgumentParser(description="Convert a BAM specification to RST")
    parser.add_argument(
        "input_file",
        type=argparse.FileType("r"),
        help="The input BAM specification file",
    )
    parser.add_argument("output_path", type=Path, help="The output path for rst files")
    args = parser.parse_args()

    # Read the input file
    with args.input_file as f:
        input_spec = yaml.load(f, Loader=yaml.FullLoader)

    with open(args.output_path / "read_formats" / "bam.paths.generated.rst", "w") as f:
        generate_bam_paths(input_spec["protocol_spec"]["contents"]["bam"], f)


if __name__ == "__main__":
    main()
