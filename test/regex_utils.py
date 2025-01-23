import re


def test_regex_with_examples(file, name, regex, examples):
    compiled_regex = re.compile(regex)

    if not examples:
        raise AssertionError(
            f"No examples provided for regex '{name}' in file '{file}'"
        )

    for i, example in enumerate(examples):
        assert compiled_regex.fullmatch(
            example
        ), f"Regex '{name}' in file '{file}' failed to match example {i}: '{example}'"
