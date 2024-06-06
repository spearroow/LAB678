import json
import os
import yaml
import xml.etree.ElementTree as ET

class FileVerifier:
    @staticmethod
    def verify_json(file_path):
        if not os.path.isfile(file_path):
            print(f"Błąd: Plik '{file_path}' nie istnieje.")
            return False

        try:
            with open(file_path, 'r') as file:
                json.load(file)
            print(f"Sukces: Plik '{file_path}' jest prawidłowym plikiem JSON.")
            return True
        except json.JSONDecodeError as e:
            print(f"Błąd: Plik '{file_path}' nie jest prawidłowym plikiem JSON. {e}")
            return False
        except Exception as e:
            print(f"Błąd: Wystąpił nieoczekiwany błąd podczas przetwarzania pliku '{file_path}'. {e}")
            return False

    @staticmethod
    def verify_yml(file_path):
        if not os.path.isfile(file_path):
            print(f"Błąd: Plik '{file_path}' nie istnieje.")
            return False

        try:
            with open(file_path, 'r') as file:
                yaml.safe_load(file)
            print(f"Sukces: Plik '{file_path}' jest prawidłowym plikiem YAML.")
            return True
        except yaml.YAMLError as e:
            print(f"Błąd: Plik '{file_path}' nie jest prawidłowym plikiem YAML. {e}")
            return False
        except Exception as e:
            print(f"Błąd: Wystąpił nieoczekiwany błąd podczas przetwarzania pliku '{file_path}'. {e}")
            return False

    @staticmethod
    def verify_xml(file_path):
        if not os.path.isfile(file_path):
            print(f"Błąd: Plik '{file_path}' nie istnieje.")
            return False

        try:
            tree = ET.parse(file_path)
            tree.getroot()
            print(f"Sukces: Plik '{file_path}' jest prawidłowym plikiem XML.")
            return True
        except ET.ParseError as e:
            print(f"Błąd: Plik '{file_path}' nie jest prawidłowym plikiem XML. {e}")
            return False
        except Exception as e:
            print(f"Błąd: Wystąpił nieoczekiwany błąd podczas przetwarzania pliku '{file_path}'. {e}")
            return False
