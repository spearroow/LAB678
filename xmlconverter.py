import xml.etree.ElementTree as ET
import json
import yaml
from file_verifier import FileVerifier

class XMLConverter:
    @staticmethod
    def convert_to_xml(data, root_name='root'):
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
    def xml_to_json(data):
        def elem_to_internal(elem, strip=1):
            d = {}
            for key, value in elem.attrib.items():
                d[key] = value
            for subelem in elem:
                v = elem_to_internal(subelem, strip=strip)
                tag = subelem.tag
                value = v
                try:
                    d[tag].append(value)
                except AttributeError:
                    d[tag] = [d[tag], value]
                except KeyError:
                    d[tag] = value
            text = elem.text
            tail = elem.tail
            if strip:
                if text:
                    text = text.strip()
                if tail:
                    tail = tail.strip()
            if text:
                d['text'] = text
            if tail:
                d['tail'] = tail
            return d
        return json.dumps(elem_to_internal(data), indent=4)

    @staticmethod
    def xml_to_yaml(data):
        def elem_to_internal(elem, strip=1):
            d = {}
            for key, value in elem.attrib.items():
                d[key] = value
            for subelem in elem:
                v = elem_to_internal(subelem, strip=strip)
                tag = subelem.tag
                value = v
                try:
                    d[tag].append(value)
                except AttributeError:
                    d[tag] = [d[tag], value]
                except KeyError:
                    d[tag] = value
            text = elem.text
            tail = elem.tail
            if strip:
                if text:
                    text = text.strip()
                if tail:
                    tail = tail.strip()
            if text:
                d['text'] = text
            if tail:
                d['tail'] = tail
            return d
        return yaml.dump(elem_to_internal(data), default_flow_style=False)

    @staticmethod
    def convert_file(input_path, output_path):
        if not FileVerifier.verify_xml(input_path):
            return False

        try:
            tree = ET.parse(input_path)
            data = tree.getroot()
        except Exception as e:
            print(f"Błąd: Nie udało się odczytać pliku wejściowego '{input_path}'. {e}")
            return False

        try:
            output_type = FileConverter.detect_file_type(output_path)
            with open(output_path, 'w') as file:
                if output_type == '.json':
                    file.write(XMLConverter.xml_to_json(data))
                elif output_type in ['.yml', '.yaml']:
                    file.write(XMLConverter.xml_to_yaml(data))
                elif output_type == '.xml':
                    file.write(ET.tostring(data, encoding='unicode'))
                else:
                    print(f"Błąd: Nieobsługiwany typ pliku wyjściowego '{output_type}'.")
                    return False
        except Exception as e:
            print(f"Błąd: Nie udało się zapisać pliku wyjściowego '{output_path}'. {e}")
            return False

        print(f"Sukces: Przekonwertowano '{input_path}' na '{output_path}'.")
        return True
