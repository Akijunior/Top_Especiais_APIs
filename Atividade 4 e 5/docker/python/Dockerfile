# Herdar de python 3.6
FROM python:3.6
# Pessoa
MAINTAINER akijunior@localhost
# Copiar o local app folder para /app
COPY ./app /app
# Setar o diretório de trabalho da aplicação
WORKDIR /app/web_apis

RUN pip install -r requirements.txt

COPY ./docker/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# pegar a imagem, copia para o servidor e depois adiciona seus arquivos e faz um commit