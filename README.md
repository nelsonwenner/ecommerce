# BOOK STORE API - REST

Um pequeno sistema de vendas de livros.

## Require
 * Python >= 3.6

## Dependencies

* Django == 2.2.8
* djangorestframework == 3.10.3
* django-rest-swagger == 2.2.0
* django-filter == 2.2.0
* djangorestframework-simplejwt == 4.3.0

## Installation

Para preparar o ambiente de execução do projeto, teremos que usar o ```virtualenv```, para comportar todas as nossas dependências.

``` bash
# Instalando vitualenv
$ pip install virtualenv

# Criando o venv do projeto.
$ virtualenv venv

# Utilizando o venv do projeto.
$ source venv/Scripts/activate

# Instalando dependências.
$ pip install -r requirements.txt
```

## Starting project

``` bash
# Criando um user admin
$ python manage.py createsuperuser

# Iniciando projeto
$ python manage.py runserver
```

## Diagram project

![bookstore-ecommerce-api](https://user-images.githubusercontent.com/40550247/70489904-baa8b500-1adb-11ea-9273-7407cb7040db.png)


``` json
Address {
    "street": "",
    "suite": "",
    "city": "",
    "zipcode": ""
}

Client {
	"name": "",
	"email": "",
	"phone": "",
	"address": Address()
}

Manager {
    "name": "",
    "email": "",
    "cpf": "",
    "salary": 0.0
}

Genre {
    "description": ""
}

Book {
    "title": "",
    "prince": 0.0,
    "stock": 0,
    "genre": Genre()
}

Author {
    "name": "",
    "email": ""
}

Write {
    "book": Book(),
    "author": Author()
}

Status {
    "message": ""
}

Creditcard {
    "flag": "",
    "number": "",
    "number_security": ""
}

Order {
    "total": 0.0,
    "client": Client(),
    "creditcard": Creditcard(),
    "manager": Manager(),
    "status": Status(),
    "total": 0.0,
    "date_created": 00-00-0000
}

ItemOrder {
    "amount": 0,
    "subtotal": 0.0,
    "book": Book(),
    "order": Order()
}
```
