import yaml

import regex_utils


def test_pattern_regex():
    with open("./patterns.yaml", "r") as f:
        patterns = yaml.safe_load(f)

        for name, pattern in patterns["patterns"].items():
            if "regex" not in pattern:
                raise AssertionError(
                    f"No regex provided for pattern '{pattern['field']}'"
                )
            if "examples" not in pattern:
                raise AssertionError(
                    f"No examples provided for pattern '{pattern['field']}'"
                )
            regex_utils.test_regex_with_examples(
                "patterns.yaml", name, pattern["regex"], pattern["examples"]
            )


def test_bam_regex():
    with open("./bam/spec.yaml", "r") as f:
        bam = yaml.safe_load(f)

        for record in bam["file"]["header_records"]:
            if "regex" not in record:
                raise AssertionError(
                    f"No regex provided for pattern '{record['field']}'"
                )
            if "examples" not in record:
                raise AssertionError(
                    f"No examples provided for regex '{record['field']}'"
                )
            regex_utils.test_regex_with_examples(
                "bam/spec.yaml", record["field"], record["regex"], record["examples"]
            )

        # for name, pattern in patterns["file"]["read_tags"].items():
        # Todo - add regex for string read tags.


def test_fastq_regex():
    with open("./fastq/header-spec.yaml", "r") as f:
        bam = yaml.safe_load(f)

        for record in bam["file"]["headers"]:
            if "regex" not in record:
                raise AssertionError(
                    f"No regex provided for pattern '{record['name']}'"
                )
            if "examples" not in record:
                raise AssertionError(
                    f"No examples provided for regex '{record['name']}'"
                )
            regex_utils.test_regex_with_examples(
                "bam/spec.yaml", record["name"], record["regex"], record["examples"]
            )

        # for name, pattern in patterns["file"]["read_tags"].items():
        # Todo - add regex for string read tags.
