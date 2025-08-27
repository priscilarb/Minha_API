# 🏋️‍♀️ Minha_API — Desafio DIO com FastAPI

Este projeto foi desenvolvido como parte do desafio da [Digital Innovation One (DIO)](https://www.dio.me/), utilizando **FastAPI**, **SQLAlchemy** e **fastapi-pagination** para criar uma API RESTful completa e assíncrona.

## 🚀 Funcionalidades

- ✅ Cadastro de atletas com dados pessoais e relacionamentos
- 🔍 Filtros por nome e CPF via query parameters
- 🎨 Resposta customizada com categoria e centro de treinamento
- 🚨 Tratamento de exceções com mensagens personalizadas (`IntegrityError`)
- 📄 Paginação de resultados com `fastapi-pagination`
- 🧰 Estrutura modular com rotas, modelos e schemas separados

## 🧪 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [fastapi-pagination](https://github.com/uriyyo/fastapi-pagination)

## 📦 Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/priscilarb/Minha_API.git
cd Minha_API

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
uvicorn dio_fastapi_api.main:app --reload
