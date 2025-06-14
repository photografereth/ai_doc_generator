from src.parsers.parser import CodeParser
from src.generators.generator import DocGenerator

def test_extract_functions():
    parser = CodeParser()
    functions = parser.extract_functions("tests/sample.py")
    assert len(functions) > 0
    assert functions[0]["name"] == "calculate_sum"

def test_generate_docstring():
    generator = DocGenerator()
    code = """
def calculate_sum(a: float, b: float) -> float:
    return a + b
    """
    docstring = generator.generate_docstring(code)
    assert "Args:" in docstring
    assert "Returns:" in docstring