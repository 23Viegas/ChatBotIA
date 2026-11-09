# ChatBotIA:

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-API-4285F4?logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

[![Testar ChatBotIA](https://img.shields.io/badge/TESTAR_NEXUSAI-ACESSAR_CHATBOT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](COLOQUE_AQUI_O_LINK_DO_CHATBOT)

## Sobre o projeto

O **ChatBotIA** é um chatbot com Inteligência Artificial desenvolvido em Python, utilizando Streamlit para a interface web e a API do Google Gemini para gerar respostas.

O objetivo do projeto é criar um assistente virtual capaz de compreender mensagens, responder perguntas e manter o contexto de uma conversa durante a sessão.

O ChatBotIA também é um projeto de aprendizado e portfólio, desenvolvido para aprofundar conhecimentos em Engenharia de Software, integração de APIs, programação modular e Inteligência Artificial Generativa.

O desenvolvimento será realizado de maneira incremental, com novas funcionalidades sendo adicionadas em versões futuras.

## Funcionalidades atuais — v0.1

- **Chat com Inteligência Artificial:** envio de perguntas e recebimento de respostas geradas pelo Google Gemini.
- **Interface interativa:** aplicação web desenvolvida com Streamlit.
- **Histórico temporário:** armazenamento das mensagens durante a sessão utilizando `st.session_state`.
- **Contexto de conversação:** envio do histórico ao modelo para permitir respostas relacionadas às mensagens anteriores.
- **Tela inicial personalizada:** apresentação do chatbot com mensagem de boas-vindas e sugestões de perguntas.
- **Indicador de carregamento:** feedback visual durante o processamento das respostas.
- **Tratamento básico de erros:** apresentação de uma mensagem amigável quando a comunicação com a API falha.
- **Configuração por variáveis de ambiente:** utilização de um arquivo `.env` para armazenar a chave da API.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| Streamlit | Desenvolvimento da interface web |
| Google Gemini | Modelo de Inteligência Artificial |
| OpenAI Python SDK | Comunicação com o endpoint compatível do Gemini |
| python-dotenv | Carregamento das variáveis de ambiente |
| Git e GitHub | Versionamento e hospedagem do código |

## Estrutura do projeto

```text
ChatBotIA/
├── src/
│   ├── main.py
│   ├── chatbot.py
│   └── config.py          # Planejado
├── tests/                 # Planejado
│   └── test_chatbot.py
├── .env                   # Privado
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### Organização dos arquivos

**`main.py`**

Responsável pela interface do usuário, exibição das mensagens e gerenciamento do histórico da conversa.

**`chatbot.py`**

Contém a lógica de integração com a API do Gemini, incluindo a configuração do cliente e o envio das mensagens ao modelo.

**`.env`**

Armazena a chave privada de acesso à API. Esse arquivo não deve ser publicado no GitHub.

**`.env.example`**

Fornece um exemplo das variáveis de ambiente necessárias para executar o projeto.

**`requirements.txt`**

Lista as bibliotecas externas necessárias para instalar e executar a aplicação.

## 🚀 Como executar o projeto

### 1. Pré-requisitos

- Python 3 instalado.
- pip disponível.
- Chave de API do Google Gemini.
- Conexão com a internet.

### 2. Clone o repositório

```bash
git clone https://github.com/23Viegas/ChatBotIA.git
cd ChatBotIA
```


### 3. Crie um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Configure a API do Gemini

Obtenha sua chave no [Google AI Studio](https://aistudio.google.com/apikey).

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como referência:

```dotenv
GEMINI_API_KEY=sua_chave_api_aqui
```

Substitua o valor de exemplo pela sua chave real.

**Importante:** nunca compartilhe sua chave nem publique o arquivo `.env` no GitHub.

### 6. Execute a aplicação

```bash
python -m streamlit run src/main.py
```

O Streamlit disponibilizará um endereço local para acessar o chatbot pelo navegador.

## Como funciona?

O funcionamento do NexusAI segue este fluxo:

1. O usuário escreve uma mensagem na interface do Streamlit.
2. O `main.py` recebe a mensagem e a adiciona ao histórico da sessão.
3. A função `mensagem_da_ia()` é chamada no `chatbot.py`.
4. O histórico da conversa é enviado à API do Gemini.
5. O modelo processa as mensagens e gera uma resposta.
6. A resposta é exibida na interface e adicionada ao histórico.

A comunicação com o Gemini utiliza o SDK Python da OpenAI por meio do endpoint compatível disponibilizado pelo Google.

## Roadmap: Próximas atualizações

O ChatBotIA será desenvolvido em etapas, com foco na evolução das funcionalidades e na qualidade do código.

### v0.1 — Chatbot funcional

- [x] Interface com Streamlit.
- [x] Integração com a API do Gemini.
- [x] Envio e recebimento de mensagens.
- [x] Histórico durante a sessão.
- [x] Tela inicial personalizada.
- [x] Indicador de carregamento.
- [x] Tratamento básico de erros.

### v0.2 — Melhorias na experiência do usuário

- [ ] Transformar as perguntas sugeridas em botões interativos.
- [ ] Adicionar botão para iniciar uma nova conversa.
- [ ] Melhorar o design e a organização da interface.
- [ ] Implementar respostas exibidas progressivamente (*streaming*).
- [ ] Aprimorar o tratamento de erros e mensagens de feedback.

### v0.3 — Histórico persistente

- [ ] Integrar um banco de dados SQLite.
- [ ] Salvar conversas permanentemente.
- [ ] Permitir visualizar conversas anteriores.
- [ ] Implementar exclusão de conversas.
- [ ] Organizar conversas por título e data.

### v0.4 — Interação com documentos

- [ ] Permitir upload de arquivos PDF.
- [ ] Extrair e processar conteúdo dos documentos.
- [ ] Implementar busca semântica.
- [ ] Utilizar RAG (*Retrieval-Augmented Generation*) para responder perguntas com base nos documentos.
- [ ] Apresentar referências aos trechos utilizados nas respostas.

### v0.5 — Personalização do assistente

- [ ] Permitir selecionar modelos de IA disponíveis.
- [ ] Criar configurações de comportamento do assistente.
- [ ] Adicionar opções de personalização da interface.
- [ ] Implementar configurações de geração de respostas.

### v1.0 — Versão estável

- [ ] Criar testes automatizados com pytest.
- [ ] Ampliar a validação de entradas.
- [ ] Implementar testes automatizados no GitHub Actions.
- [ ] Revisar o gerenciamento de erros e limites da API.
- [ ] Melhorar a documentação técnica.
- [ ] Publicar uma versão estável no Streamlit Community Cloud.

**Observação:** o roadmap representa funcionalidades planejadas e poderá sofrer alterações conforme o desenvolvimento do projeto.

## Segurança e privacidade

O ChatBotIA utiliza variáveis de ambiente para evitar que chaves de API sejam armazenadas diretamente no código-fonte.

O arquivo `.env` deve permanecer fora do controle de versão.

As mensagens enviadas pelo usuário são encaminhadas à API do Google Gemini para processamento.

Na versão atual, o histórico é mantido na sessão do Streamlit e não é armazenado permanentemente pelo aplicativo. Isso não significa que os dados enviados à API não estejam sujeitos às políticas de tratamento de dados do provedor.

Recomenda-se não enviar senhas, documentos confidenciais ou outras informações sensíveis ao chatbot.

## Objetivos de aprendizado

Este projeto busca desenvolver habilidades práticas em:

- Programação Python.
- Desenvolvimento de aplicações web.
- Integração com APIs REST e SDKs.
- Inteligência Artificial Generativa.
- Gerenciamento de estado em aplicações.
- Modularização e organização de código.
- Tratamento de exceções.
- Gerenciamento de variáveis de ambiente.
- Versionamento com Git e GitHub.
- Testes automatizados e bancos de dados em versões futuras.

## Status do projeto

**Em desenvolvimento — versão 0.1**

O ChatBotIA já possui uma implementação funcional de conversação com Inteligência Artificial. Novas funcionalidades e melhorias serão incorporadas progressivamente.

---

Desenvolvido como projeto pessoal de estudo e portfólio em Python, Engenharia de Software e Inteligência Artificial.