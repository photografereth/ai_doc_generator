#!/usr/bin/env python3
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
