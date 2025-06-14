"""Parser factory"""
from pathlib import Path
from .base import BaseParser
from .python_parser import PythonParser

class ParserFactory:
    def __init__(self):
        self._parsers = {'.py': PythonParser}
    
    def get_parser(self, extension: str):
        return self._parsers.get(extension.lower(), lambda: None)()
