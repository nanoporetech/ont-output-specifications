from pathlib import Path
import yaml


def spec_to_path(spec: str) -> Path:
    if spec == "bam":
        return "bam/spec.yaml"
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
