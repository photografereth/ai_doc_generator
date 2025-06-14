"""Basic usage example"""
from pathlib import Path
from ai_doc_generator import Config, DocumentationGenerator

def main():
    config = Config.load()
    generator = DocumentationGenerator(config)
    result = generator.generate(Path("."))
    print(f"Generated: {result.output_path}")

if __name__ == "__main__":
    main()
