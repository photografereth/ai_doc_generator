##### **`src/cli.py`**

import argparse
from src.parser import CodeParser
from src.generator import DocGenerator

def main():
    parser = argparse.ArgumentParser(description="Gerador Automático de Documentação com IA")
    parser.add_argument("file", help="Caminho para o arquivo Python")
    parser.add_argument("--output", default="README.md", help="Arquivo de saída para o README")
    args = parser.parse_args()

    # Inicializa parser e gerador
    code_parser = CodeParser()
    doc_generator = DocGenerator()

    # Extrai funções
    functions = code_parser.extract_functions(args.file)
    
    # Gera README
    readme_content = doc_generator.generate_readme("Projeto Exemplo", functions)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # Gera e exibe docstrings
    for func in functions:
        docstring = doc_generator.generate_docstring(func["code"])
        print(f"Docstring para {func['name']}:\n{docstring}\n")

if __name__ == "__main__":
    main()