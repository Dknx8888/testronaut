import yaml

def load_pipeline(file_path):
    """Load and parse a YAML file containing the CI/CD pipeline configuration."""
    with open(file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            return data
        except yaml.YAMLError as exc:
            print("Error parsing YAML:", exc)
            return None
