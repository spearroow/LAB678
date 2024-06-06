import os

class FileConverter:
    @staticmethod
    def detect_file_type(file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower()
