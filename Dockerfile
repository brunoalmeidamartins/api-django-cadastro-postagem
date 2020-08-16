FROM python:3.6.11-stretch

RUN apt-get update && apt-get upgrade -y

RUN mkdir -p /app/

WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app/

COPY . /app/

COPY settings_docker.py /app/django_rest/django_rest/settings.py

COPY deploy.sh /app/deploy.sh

RUN chmod +x deploy.sh

EXPOSE 8000

CMD ["sh", "deploy.sh"]