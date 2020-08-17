# API Djando Cadastro Postagens

## Esta é uma API de Cadastro de Postagens com autenticação de usuário.

Para executar o projeto, crie um banco de dados em seu MYSQL e corriga os parâmetros do arquivo 'settings.py' localizado na pasta 'django_rest/django_rest/'.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT': '',
    }
}
```

Utilize o arquivo 'requirements.txt' para instalar as bibliotecas necessárias para rodar o projeto.
```
pip install -r requirements.txt
```

Rode os comandos abaixo para criar as tabelas no banco de dados.
```
python django_rest/manage.py makemigrations
```
```
python django_rest/manage.py migrates
```

Rode a api com o comando:
```
python django_rest/manage.py runserver 0.0.0.0:8000
```

É necessário criar um superuser para acessar o  módulo admin do Django e poder criar uma Applications de acesso a API.
```  
python django_rest/manage.py createsuperuser
```

Acesse a url http://IP_SERVER:8000/admin/ e faça login no módulo. Em seguida, adicione uma Applications do Menu DJANGO OAUTH TOOLKIT.

1. Selecione 'Confidential' no item 'Client type'.
2. Selecione 'Resource owner password-based' no item 'Authorization grant type'.
3. Coloque um nome qualquer no item 'Name'.
4. Grave o 'Client id' e o 'Client secret1. Eles serão usados para autenticação na API.
5. Clique em 'SALVAR'.

## Para utilizar o docker

Para rodar com o docker, basta ter o docker-compose instalado em sua máquina e executar o 'docker-compose.yml'.

```
docker-compose up --build -d
```

Em seguida, execute os passos de criação de um superuser dentro do container e adicione uma Application no módulo DJANGO OAUTH TOOLKIT. 

```
docker exec ID_CONTAINER_API -it /bin/bash
```
```
python django_rest/manage.py createsuperuser
```

Se estiver rodando o container localmente, acesse:
```
http://0.0.0.0:8000/admin
```

## Deploy na AWS
Há uma instância rodando na AWS para execução de testes na API. Utilize os dados fornecidos abaixo: 
```
IP:3.129.125.154
CLIENT_ID:8lKBeQ5hjhpjpFsBk9MrOhKjZsjLd8cWOO6RVlI1
CLIENT_SECRET:0pqwYN0LfwWpsLBz1yO8EBM31ZzKmp8ULIxwLoHn1g6hgLh61Sp0Aavn71VtHDUvqVV7ZDyTQRvubxWWR2s3WFsCJ5plEW2j79CgVK8ChyGafMqpILpzm0pkm1LRmbOQ
```

Caso não queira criar um usuário novo, utilize:
```
USERNAME: brunomartins
EMAIL: brunomartins@mail.com
PASSWORD: 123456
```

## Rotas da API
Utilize o Postman para executar chamadas na API.
### Rotas sem autenticação
[Cadastrar Usuário]: http://IP_SERVER:8000/api/usuarios/
Método: POST
Body:
{
	"username": "",
	"email": "",
	"password": ""
}

[Login Usuário] = http://IP_SERVER:8000/oauth/token/
Método: POST
Body:
{
	"grant_type": "password",
	"client_id": "",
	"client_secret": "",
	"username":"",
	"email":"",
	"password": ""
}
### Rotas autenticadas
Para utilizar as rotas autenticadas, forneça um token válido - obtido através do [Login Usuário]. Os tokens serão do tipo 'Bearer'.

[Listar Postagens] = http://IP_SERVER:8000/api/postagens/
Método: GET
Headers: "Authorization" "Bearer 'token_valido'"

[Cadastrar Postagens] = http://IP_SERVER:8000/api/postagens/
Método: POST
Headers: "Authorization" "Bearer 'token_valido'"
Body:
{
    "titulo": "",
    "descricao": "",
    "url_imagem": ""
}

[Listar Postagem ID] = http://IP_SERVER:8000/api/postagens/<int:id>
Método: GET
Headers: "Authorization" "Bearer 'token_valido'"

[Editar Postagem ID] = http://IP_SERVER:8000/api/postagens/<int:id>
Método: PUT
Headers: "Authorization" "Bearer 'token_valido'"
Body:
{
    "titulo": "",
    "descricao": "",
    "url_imagem": ""
}

[Deletar Postagem ID] = http://IP_SERVER:8000/api/postagens/<int:id>
Método: DELETE
Headers: "Authorization" "Bearer 'token_valido'"