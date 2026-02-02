import yaml


def load_schema(schema_path):
    with open(schema_path, "r") as file:
        return yaml.safe_load(file)