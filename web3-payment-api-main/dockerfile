# Dockerfile

FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /code

# Copia o arquivo requirements.txt para o contêiner
COPY ./requirements.txt /code/requirements.txt

# Instala as dependências
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia o código da aplicação para o contêiner
COPY ./app /code/app

# Executa o servidor Uvicorn com hot reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
