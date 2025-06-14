import requests

class DocGenerator:
    def __init__(self, api_key=None):
        self.api_key = api_key or "YOUR_API_KEY"  # Substitua pela chave da Grok API

    def generate_docstring(self, code_snippet):
        """Gera docstring para um trecho de código usando IA."""
        # Mock da chamada à API (substitua pela Grok API real)
        prompt = f"""
        Analise o código Python abaixo e gere uma docstring no estilo Google:

        ```python
        {code_snippet}
        ```

        Retorne apenas a docstring formatada.
        """
        # Simulação da resposta da API
        mock_response = f'''
        """Calcula a soma de dois números reais.

        Args:
            a (float): O primeiro número.
            b (float): Segundo número.

        Returns:
            float: A soma de a e b.
        """
        '''
        # Exemplo de chamada real à Grok API (descomente para usar)
        """
        response = requests.post(
            "https://api.x.ai/grok",
            json={"prompt": prompt},
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        return response.json().get("result", "")
        """
        return mock_response

    def generate_readme(self, project_name, functions):
        """Gera um README básico para o projeto."""
        readme = f"""
# {project_name}

## Descrição
Um projeto Python que contém funções úteis.

## Instalação
```bash
pip install -r requirements.txt
"""