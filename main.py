import argparse
from file_verifier import FileVerifier
from json_converter import JSONConverter
from yaml_converter import YAMLConverter
from xml_converter import XMLConverter
from file_converter import FileConverter

def main():
    parser = argparse.ArgumentParser(description='Weryfikuj i konwertuj pliki JSON, YAML lub XML.')
    parser.add_argument('--verify-json', type=str, help='Ścieżka do pliku JSON do weryfikacji.')
    parser.add_argument('--verify-yml', type=str, help='Ścieżka do pliku YAML do weryfikacji.')
    parser.add_argument('--verify-xml', type=str, help='Ścieżka do pliku XML do weryfikacji.')
    parser.add_argument('--convert', nargs=2, help='Konwertuj plik1 na plik2. Wykrywa typy plików na podstawie rozszerzenia.')

    args = parser.parse_args()

    if args.verify_json:
        FileVerifier.verify_json(args.verify_json)
    elif args.verify_yml:
        FileVerifier.verify_yml(args.verify_yml)
    elif args.verify_xml:
        FileVerifier.verify_xml(args.verify_xml)
    elif args.convert:
        input_path, output_path = args.convert
        input_type = FileConverter.detect_file_type(input_path)
        if input_type == '.json':
            JSONConverter.convert_file(input_path, output_path)
        elif input_type in ['.yml', '.yaml']:
            YAMLConverter.convert_file(input_path, output_path)
        elif input_type == '.xml':
            XMLConverter.convert_file(input_path, output_path)
        else:
            print(f"Błąd: Nieobsługiwany typ pliku wejściowego '{input_type}'.")
    else:
        print("Nie podano żadnych argumentów. Użyj --help, aby zobaczyć dostępne opcje.")

if __name__ == "__main__":
    main()
