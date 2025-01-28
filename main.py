import ast
from pathlib import Path
import tabulate
import yaml


def spec_to_path(spec: str) -> Path:
    if spec == "bam":
        return "bam/spec.yaml"
    elif spec == "fastq":
        return "fastq/header-spec.yaml"
    elif spec == "pod5":
        return "pod5/spec.yaml"
    return Path(f"{spec}.yaml")


def define_env(env):
    @env.macro
    def spec_value(spec: str, key: str) -> str:
        """
        Load a value from a specification file.

        :param spec: The identifier of the specification file to load.
        :param key: The key to load from the specification file,
            eg: "protocol_spec.contents.bam.bai_path"
        :return: The value from the specification file.
        """
        path = spec_to_path(spec)
        with open(path) as f:
            loaded = yaml.safe_load(f)

            keys = key.split(".")

            value = loaded
            for k in keys:
                value = value[k]

            return str(value)

    @env.macro
    def make_table_from_mapping(key_title: str, value_title: str, values: str) -> str:
        """
        Create a table from a dictionary.

        :param key_title: The title of the key column.
        :param value_title: The title of the value column.
        :param values: The json compatible mapping to
            create the table from, in string form.
        """

        values_json = ast.literal_eval(values)
        list_values = [[key, value] for key, value in values_json.items()]
        return tabulate.tabulate(
            list_values, headers=[key_title, value_title], tablefmt="pipe"
        )

    @env.macro
    def warning(message: str) -> str:
        """
        Create a warning block.

        :param message: The message to display in the warning block.
        """
        return (
            '<span class="admonition warning"><p class="admonition-title">'
            f"{message}</p></span>"
        )
