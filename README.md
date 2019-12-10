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

![bookstore-api](https://user-images.githubusercontent.com/40550247/70279430-3f6e9880-1795-11ea-8ac2-7cee757dab7a.png)
