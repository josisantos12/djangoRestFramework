# Use uma imagem base oficial do Python
FROM python:3.10-slim-bookworm

# Configure a variável de ambiente para desativar buffer do Python
ENV PYTHONUNBUFFERED=1

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos de dependências
COPY requirements.txt /app/

# Instale as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o container
COPY . /app/

# Exponha a porta em que o Django irá rodar
EXPOSE 8000

# Comando para rodar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]