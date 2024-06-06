import yaml
import json
import xml.etree.ElementTree as ET
from file_verifier import FileVerifier

class YAMLConverter:
    @staticmethod
    def convert_to_yaml(data):
        return yaml.dump(data, default_flow_style=False)

    @staticmethod
    def yaml_to_json(data):
        return json.dumps(data, indent=4)

    @staticmethod
    def yaml_to_xml(data, root_name='root'):
        root = ET.Element(root_name)
        def build_tree(element, data):
            if isinstance(data, dict):
                for key, value in data.items():
                    child = ET.SubElement(element, key)
                    build_tree(child, value)
            elif isinstance(data, list):
                for item in data:
                    child = ET.SubElement(element, 'item')
                    build_tree(child, item)
            else:
                element.text = str(data)
        build_tree(root, data)
        return ET.tostring(root, encoding='unicode')

    @staticmethod
    def convert_file(input_path, output_path):
        if not FileVerifier.verify_yml(input_path):
            return False

        try:
            with open(input_path, 'r') as file:
                data = yaml.safe_load(file)
        except Exception as e:
            print(f"Błąd: Nie udało się odczytać pliku wejściowego '{input_path}'. {e}")
            return False

        try:
            output_type = FileConverter.detect_file_type(output_path)
            with open(output_path, 'w') as file:
                if output_type == '.json':
                    file.write(YAMLConverter.yaml_to_json(data))
                elif output_type in ['.yml', '.yaml']:
                    file.write(YAMLConverter.convert_to_yaml(data))
                elif output_type == '.xml':
                    file.write(YAMLConverter.yaml_to_xml(data))
                else:
                    print(f"Błąd: Nieobsługiwany typ pliku wyjściowego '{output_type}'.")
                    return False
        except Exception as e:
            print(f"Błąd: Nie udało się zapisać pliku wyjściowego '{output_path}'. {e}")
            return False

        print(f"Sukces: Przekonwertowano '{input_path}' na '{output_path}'.")
        return True
