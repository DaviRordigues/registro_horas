# Usar uma imagem base do Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    libpq-dev \
    libaio1 \
    && rm -rf /var/lib/apt/lists/*

# Copiar o arquivo de requisitos
COPY requirements.txt /app/

# Instalar dependências do Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar o código do projeto
COPY . /app/

# Configurar variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=viaturas_admin/settings
ENV PYTHONUNBUFFERED=1

# Expor a porta que o Django usará
EXPOSE 80

# Comando para rodar as migrações e iniciar o servidor Django
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:80"]