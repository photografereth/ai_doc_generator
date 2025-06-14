"""Configuration management"""
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
