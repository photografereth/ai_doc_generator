from tree_sitter import Language, Parser
import os

class CodeParser:
    def __init__(self):
        # Configurar Tree-sitter para Python
        Language.build_library(
            "build/python.so",
            ["./README.md"]  # Substitua pelo caminho correto
        )
        self.PY_LANGUAGE = Language("build/python.so", "python")
        self.parser = Parser()
        self.parser.set_language(self.PY_LANGUAGE)

    def extract_functions(self, file_path):
        """Extrai funções de um arquivo Python."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo {file_path} não encontrado")
        
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        tree = self.parser.parse(code.encode())
        functions = []
        
        # Percorre a AST para encontrar funções
        for node in tree.root_node.children:
            if node.type == "function_definition":
                func_name = node.child_by_field_name("name").text.decode()
                func_code = code[node.start_byte:node.end_byte]
                functions.append({"name": func_name, "code": func_code})
        
        return functions