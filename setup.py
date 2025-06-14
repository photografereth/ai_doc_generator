#!/usr/bin/env python3
"""
Script otimizado para inicializar o projeto AI Doc Generator
Execute: python init_project.py
"""

import os
from pathlib import Path

def create_directory_structure():
    """Cria a estrutura de diretórios do projeto"""
    directories = [
        "src/ai_doc_generator/core", "src/ai_doc_generator/parsers",
        "src/ai_doc_generator/generators", "src/ai_doc_generator/templates",
        "src/ai_doc_generator/utils", "tests/unit", "tests/integration",
        "docs", "examples", "config", ".github/workflows"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Criado: {directory}")

def create_core_files():
    """Cria arquivos principais"""
    files = {
        # Main package init
        "src/ai_doc_generator/__init__.py": '''"""AI Doc Generator"""
__version__ = "0.1.0"
from .core.generator import DocumentationGenerator
from .core.config import Config
__all__ = ["DocumentationGenerator", "Config"]
''',

        # Configuration
        "src/ai_doc_generator/core/config.py": '''"""Configuration management"""
from dataclasses import dataclass
from pathlib import Path
import yaml

@dataclass
class Config:
    ai_provider: str = "openai"
    model: str = "gpt-4"
    output_format: str = "markdown"
    output_dir: str = "./docs"
    
    @classmethod
    def load(cls, config_path=None):
        if config_path and Path(config_path).exists():
            with open(config_path) as f:
                data = yaml.safe_load(f)
                return cls(**data)
        return cls()
''',

        # Main generator
        "src/ai_doc_generator/core/generator.py": '''"""Main documentation generator"""
from pathlib import Path
from dataclasses import dataclass
from typing import List
from .config import Config

@dataclass
class GenerationResult:
    success: bool
    output_path: Path
    files_processed: int

class DocumentationGenerator:
    def __init__(self, config: Config):
        self.config = config
    
    def generate(self, source_path: Path) -> GenerationResult:
        # Implementation here
        return GenerationResult(True, Path(self.config.output_dir), 0)
''',

        # Parser factory
        "src/ai_doc_generator/parsers/factory.py": '''"""Parser factory"""
from pathlib import Path
from .base import BaseParser
from .python_parser import PythonParser

class ParserFactory:
    def __init__(self):
        self._parsers = {'.py': PythonParser}
    
    def get_parser(self, extension: str):
        return self._parsers.get(extension.lower(), lambda: None)()
''',

        # Base parser
        "src/ai_doc_generator/parsers/base.py": '''"""Base parser interface"""
from abc import ABC, abstractmethod
from pathlib import Path

class BaseParser(ABC):
    @abstractmethod
    def parse(self, file_path: Path):
        pass
    
    def _read_file(self, file_path: Path) -> str:
        try:
            return file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            return file_path.read_text(encoding='latin-1')
''',

        # Python parser
        "src/ai_doc_generator/parsers/python_parser.py": '''"""Python parser"""
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
''',

        # CLI
        "src/ai_doc_generator/cli.py": '''#!/usr/bin/env python3
"""CLI for AI Doc Generator"""
import click
from pathlib import Path
from .core.config import Config
from .core.generator import DocumentationGenerator

@click.command()
@click.argument('path', default='.')
@click.option('--config', '-c', help='Config file')
@click.option('--output', '-o', help='Output directory')
@click.option('--format', '-f', help='Output format')
def main(path, config, output, format):
    """Generate AI documentation"""
    config_obj = Config.load(config)
    if output: config_obj.output_dir = output
    if format: config_obj.output_format = format
    
    generator = DocumentationGenerator(config_obj)
    result = generator.generate(Path(path))
    
    if result.success:
        click.echo(f"✅ Docs generated at: {result.output_path}")
    else:
        click.echo("❌ Generation failed")

if __name__ == "__main__":
    main()
''',

        # Requirements
        "requirements.txt": '''openai>=1.0.0
click>=8.0.0
pyyaml>=6.0
rich>=13.0.0
''',

        # Config example
        ".env.example": '''OPENAI_API_KEY=your_key_here
DEFAULT_AI_PROVIDER=openai
DEFAULT_MODEL=gpt-4
''',

        # Default config
        "config/default.yaml": '''ai_provider: "openai"
model: "gpt-4"
output_format: "markdown"
output_dir: "./docs"
''',

        # Gitignore
        ".gitignore": '''__pycache__/
*.pyc
.env
.venv/
dist/
build/
*.egg-info/
.cache/
logs/
''',

        # README
        "README.md": '''# AI Doc Generator

🤖 AI-powered documentation generator

## Quick Start

```bash
pip install -e .
ai-doc-gen ./src --format markdown
```

## Features

- Multi-language support (Python, JS, etc.)
- Multiple AI providers (OpenAI, Anthropic)
- Flexible output formats
- Smart code parsing

## Configuration

Create `.env`:
```
OPENAI_API_KEY=your_key
```

## Usage

```python
from ai_doc_generator import DocumentationGenerator, Config

config = Config.load()
generator = DocumentationGenerator(config)
result = generator.generate(Path("./src"))
```
''',

        # Example
        "examples/basic_usage.py": '''"""Basic usage example"""
from pathlib import Path
from ai_doc_generator import Config, DocumentationGenerator

def main():
    config = Config.load()
    generator = DocumentationGenerator(config)
    result = generator.generate(Path("."))
    print(f"Generated: {result.output_path}")

if __name__ == "__main__":
    main()
''',
    }
    
    # Create __init__.py files
    init_files = [
        "src/ai_doc_generator/core/__init__.py",
        "src/ai_doc_generator/parsers/__init__.py", 
        "src/ai_doc_generator/generators/__init__.py",
        "tests/__init__.py"
    ]
    
    for init_file in init_files:
        files[init_file] = ""
    
    for file_path, content in files.items():
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ Criado: {file_path}")

def main():
    """Executa a inicialização do projeto"""
    print("🚀 Inicializando AI Doc Generator...")
    
    create_directory_structure()
    create_core_files()
    
    print("\n✅ Projeto inicializado com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. cd ai_doc_generator")
    print("2. pip install -r requirements.txt")
    print("3. cp .env.example .env")
    print("4. Configure suas API keys no .env")
    print("5. python -m ai_doc_generator.cli --help")

if __name__ == "__main__":
    main()