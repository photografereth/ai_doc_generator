in development...

# AI Doc Generator

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
