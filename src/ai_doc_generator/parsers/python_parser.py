"""Python parser"""
import ast
from pathlib import Path
from .base import BaseParser

class PythonParser(BaseParser):
    def parse(self, file_path: Path):
        content = self._read_file(file_path)
        try:
            tree = ast.parse(content)
            return {
                'path': str(file_path),
                'functions': self._extract_functions(tree),
                'classes': self._extract_classes(tree),
                'imports': self._extract_imports(tree)
            }
        except SyntaxError:
            return {'path': str(file_path), 'error': 'Syntax error'}
    
    def _extract_functions(self, tree):
        return [{'name': node.name, 'docstring': ast.get_docstring(node)}
                for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    
    def _extract_classes(self, tree):
        return [{'name': node.name, 'docstring': ast.get_docstring(node)}
                for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    
    def _extract_imports(self, tree):
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend([alias.name for alias in node.names])
        return imports
