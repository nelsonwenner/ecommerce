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
# Criando o venv do projeto.
$ virtualenv venv

# Utilizando o venv do projeto.
$ source venv/Scripts/activate

# Instalando dependências.
$ pip install -r requirements.txt
```

## Starting project

``` bash
$ python manage.py runserver
```

## Diagram project

![bookstore-api](https://user-images.githubusercontent.com/40550247/70279430-3f6e9880-1795-11ea-8ac2-7cee757dab7a.png)

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

Administrator {
    "name": "",
    "email": "",
    "cpf": "",
    "salary": 0.0
}

Employee {
    "name": "",
    "email": "",
    "cpf": "",
    "salary": 0.0,
    "Administrator": Administrator()
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

Sale {
    "total": 0.0,
    "date_created": 00-00-0000,
    "status": Status(),
    "employee": Employee(),
    "client": Client()
}

Itemsale {
    "amount": 0,
    "subtotal": 0.0,
    "book": Book(),
    "sale": Sale()
}
```

## Features

|                                  Features                                    |     Book Store     |
| :--------------------------------------------------------------------------: | :----------------: |
| Somente administradores e admin criam status e o modificam                   |         ✔️          |
| Somente administradores e admin criam e modificam livros                     |         ✔️          |
| Funcionarios podem modificar a quantidade de estoques de livros              |         ✔️          |
| Funcionarios e administradores podem criar vendas                            |         ✔️          |
| Funcionarios e administradores podem mudar o status das vendas               |         ✔️          |
| Não pode adicionar items a uma venda com status compra finalizada            |         ✔️          |
| O sistema é responsavel por realizar todos os calculos das vendas            |         ✔️          |
| O sistema gerencia a quantidade de stock dos livros, ao adiciona-lo a venda  |         ✔️          |
| Somento administradores e admin podem ver os relatórios                      |         ✔️          |

## Reports

|                          Reports                                             |     Book Store     |
| :--------------------------------------------------------------------------: | :----------------: |
| Exibe o valor total em dinheiro de todos os livros vendidos pelo funcionario |         ✔️          |
| Exibe a quantidade de clientes que o funcionario atendeu                     |         ✔️          |
| Exibe a quantidade total de livros vendidos pelo funcionario                 |         ✔️          |
| Exibe os livros comprados pelo cliente                                       |         ✔️          |
| Exibe todas as compras do cliente                                            |         ✔️          |
