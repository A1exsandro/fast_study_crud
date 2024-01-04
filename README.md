# Start
uvicorn app.main:app --host=localhost --port=8888 --reload

# Alembic
* alembic init name_choice
* alembic revision --autogenerate -m "your description"
* alembic upgrade head

# Criar e ativar ambiente Virtual Windows
* python -m venv .venv
* .venv\Scripts\activate

# Criar e ativar ambiente Virtual Linux
* python3 -m venv .venv
* . .venv/bin/activate

# Instalar dependências
* pip install -r requirements.txt

# Alguns Comandos git
* git merge -Xours nome-do-ramo-fonte
* git merge -Xtheirs nome-do-ramo-fonte
