**2. Prompt para Claude (Aperfeiçoamento do Repositório)**

Abaixo está um prompt estruturado para enviar ao Claude, com o objetivo de melhorar o repositório. Ele foca em adicionar funcionalidades, melhorar a robustez e torná-lo mais atrativo para o GitHub.

**Prompt para Claude**

Olá, Claude! Estou desenvolvendo um projeto open-source no GitHub chamado "AI Doc Generator", uma ferramenta em Python que analisa código-fonte (inicialmente Python) e gera documentação automática (docstrings e README) usando IA. Abaixo está o código inicial e a descrição do projeto. Minha meta é torná-lo mais robusto, escalável e atrativo para contribuidores no GitHub. Por favor, sugira melhorias específicas e forneça o código correspondente para implementar essas melhorias.

**Código Inicial**
[Insira o conteúdo dos arquivos acima: src/parser.py, src/generator.py, src/cli.py, tests/test_generator.py, requirements.txt, .github/workflows/ci.yml, README.md]

**Funcionalidades Atuais**
- Analisa código Python com Tree-sitter para extrair funções.
- Gera docstrings no estilo Google (usando uma API de IA mockada).
- Cria um README básico com informações do projeto e funções.
- CLI para executar a ferramenta.
- Testes unitários com pytest.
- CI com GitHub Actions.

**Objetivos de Aperfeiçoamento**
1. **Novas Funcionalidades**:
   - Adicionar suporte para gerar diagramas (ex.: Mermaid ou PlantUML) para funções ou classes.
   - Implementar suporte para outras linguagens (ex.: JavaScript) usando Tree-sitter.
   - Adicionar geração de changelogs com base em commits.
2. **Robustez**:
   - Melhorar tratamento de erros (ex.: arquivos inválidos, falhas na API).
   - Adicionar validação de configuração (ex.: arquivo YAML para templates).
   - Garantir que docstrings sejam injetados no código original sem sobrescrever.
3. **Experiência do Usuário**:
   - Criar uma interface web simples com Streamlit para upload de arquivos e visualização da documentação.
   - Adicionar opções de personalização (ex.: estilo de docstring, tom do README).
4. **Atratividade no GitHub**:
   - Melhorar o README com badges, capturas de tela e exemplos práticos.
   - Adicionar templates para issues e pull requests.
   - Sugerir estratégias para atrair contribuidores.

**Instruções**
- Forneça o código completo para as melhorias sugeridas, mantendo a estrutura modular existente (src/parser.py, src/generator.py, etc.).
- Inclua explicações claras sobre cada mudança e como ela atende aos objetivos.
- Adicione instruções para testar as novas funcionalidades.
- Evite usar APIs ou ferramentas que não sejam open-source ou que exijam pagamento (exceto Grok API, que usarei separadamente).
- Se possível, inclua um exemplo de diagrama gerado (Mermaid ou PlantUML).

**Saída Esperada**
- Código atualizado para cada arquivo modificado.
- Novo README com badges e exemplos.
- Arquivos de configuração adicionais (ex.: templates de issues/PR, arquivo YAML).
- Explicações detalhando as mudanças.
- Instruções de teste.

Obrigado por ajudar a tornar meu repositório mais profissional e útil!