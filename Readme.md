# Chatbot Analyzer

**Chatbot Analyzer** é uma ferramenta web para analisar logs de conversas de chatbots. O projeto permite a análise de arquivos CSV contendo registros de interações com um chatbot e fornece recomendações para melhorar a curadoria e a cobertura das intenções.

## Funcionalidades

- **Análise de Logs**: Carregue um arquivo CSV com logs de conversa do chatbot.
- **Recomendações e Curadoria**: Receba sugestões para melhorar a precisão e a cobertura do chatbot, incluindo novas frases e otimizações de intenções.
- **Interface Intuitiva**: Interface web desenvolvida com Bootstrap, com indicadores de carregamento enquanto o arquivo é processado.

## Requisitos

- Python 3.x
- Biblioteca `Flask` para o servidor web
- Biblioteca `pandas` para manipulação de dados
- Biblioteca `openai` para interação com o modelo GPT
- Biblioteca `python-dotenv` para gerenciar variáveis de ambiente
- Biblioteca `Bootstrap` para estilização da interface

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/chatbot-analyzer.git
   ```
2. Navegue para o diretório do projeto:
   ```bash
   cd chatbot-analyzer
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No macOS/Linux
   ```
4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Uso

1. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
2. Acesse `http://127.0.0.1:5000` no seu navegador.
3. Carregue um arquivo CSV com logs de conversa e clique em "Enviar" para receber recomendações e sugestões de curadoria.

## Estrutura do Projeto

- `app.py`: Código principal do aplicativo Flask.
- `templates/`: Contém os arquivos HTML para as páginas web.
- `static/css/`: Contém os arquivos CSS para estilização.
- `static/images/`: Contém imagens como o GIF de carregamento.
- `.env`: Arquivo para variáveis de ambiente (não incluído no repositório).
- `requirements.txt`: Lista de dependências do projeto.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
