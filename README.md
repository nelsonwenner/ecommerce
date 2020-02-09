<h1 align="center">
  <img src="https://user-images.githubusercontent.com/40550247/72228004-81071600-3581-11ea-9972-1cbe906001ed.png" width="120px" />
</h1>

<h1 align="center">
  BOOK STORE API - REST
</h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/nelsondiaas/bookstore-api?color=%2304D361">

  <a href="https://github.com/nelsondiaas">
    <img alt="Made by @nelsondiaas" src="https://img.shields.io/badge/made%20by-%40nelsondiaas-%2304D361">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361">

  <a href="https://github.com/nelsondiaas/bookstore-api/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/nelsondiaas/bookstore-api?style=social">
  </a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#diagram-project">Diagram</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#endpoints-access">Endpoints Access</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

## Require
 * Python (>= 3.6)

## Getting Started
1. Fork este repositório e clone em sua máquina.
2. Mude o diretório para `bookstore-api` onde você o clonou.
3. No terminal, execute:

``` bash
# Criando o venv do projeto.
$ python -m venv venv

# Utilizando o venv do projeto.
$ source venv/Scripts/activate

# Instalando dependências.
$ pip install -r requirements.txt

# Criando um user admin
$ python manage.py createsuperuser

# Iniciando projeto
$ python manage.py runserver
```
  4. Abra o host [localhost:8000](http://localhost:8000) e comece a usá-lo.

## Diagram project

![bookstore-ecommerce-api](https://user-images.githubusercontent.com/40550247/74076709-c0961600-49f8-11ea-807c-2af80d6307e1.png)

## Endpoints access

<details><summary><b>Tokens</b></summary><blockquote>

#### Allowed methods = [POST]

[POST] http://www.hostname.com/api-token/

##### Sample request

```json
{
    "email": "",
	"password": ""
}
```
##### Sample response

```json
{
    "refresh": "",
    "token": "",
    "id": 1,
    "username": "",
    "email": "",
    "is_staff": false
}
```

[POST] http://www.hostname.com/api-token/refresh/
 
##### Sample request

```json
{
    "refresh": "",
}
```

##### Sample response

```json
{
    "token": "",
}
```

</details>

<details><summary><b>Users</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/users/

##### Sample request

```json
{
    "username": "",
    "email": "",
    "password": "",
    "is_staff": true
}
```

[GET] http://www.hostname.com/users/

##### Sample response

```json
{
    "id": 1,
    "url": "",
    "username": "",
    "email": "",
    "is_staff": true
}
```

</details>

<details><summary><b>Clients</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/clients/

##### Sample request

```json
{
    "name": "",
    "email": "",
    "password": "",
    "phone": "",
    "credit_card": Creditcart(),
    "address": Client()
}
```

[GET] http://www.hostname.com/clients/

##### Sample response

```json
{
    "name": "",
    "email": "",
    "password": "",
    "phone": "",
    "credit_card": Creditcart(),
    "address": Client()
}
```

</details>

<details><summary><b>Address</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/address/

##### Sample request

```json
{
    "street": "",
    "suite": "",
    "city": "",
    "zipcode": ""
}
```

[GET] http://www.hostname.com/address/

##### Sample response

```json
{
    "street": "",
    "suite": "",
    "city": "",
    "zipcode": ""
}
```

</details>

<details><summary><b>Managers</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/managers/

##### Sample request

```json
{
    "name": "",
    "email": "",
    "password": "",
    "cpf": "",
    "salary": 0.0
}
```

[GET] http://www.hostname.com/managers/

##### Sample response

```json
{
    "name": "",
    "email": "",
    "password": "",
    "cpf": "",
    "salary": 0.0
}
```

</details>

<details><summary><b>Status</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/status/

##### Sample request

```json
{
    "message": ""
}
```

[GET] http://www.hostname.com/status/

##### Sample response

```json
{
    "message": ""
}
```

</details>

<details><summary><b>Genres</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/genres/

##### Sample request

```json
{
    "description": ""
}
```

[GET] http://www.hostname.com/genres/

##### Sample response

```json
{
    "description": ""
}
```

</details>

<details><summary><b>Authors</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/authors/

##### Sample request

```json
{
    "name": "",
    "email": ""
}
```

[GET] http://www.hostname.com/authors/

##### Sample response

```json
{
    "name": "",
    "email": ""
}
```

</details>

<details><summary><b>Books</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/books/

##### Sample request

```json
{
    "title": "",
    "prince": 0,
    "stock": 0,
    "genre": Genre(),
    "image": ""
}
```

[GET] http://www.hostname.com/books/

##### Sample response

```json
{
    "title": "",
    "prince": 0,
    "stock": 0,
    "genre": Genre(),
    "image": ""
}
```

</details>

<details><summary><b>Writes</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/writes/

##### Sample request

```json
{
    "author": Author(),
    "book": Book()
}
```

[GET] http://www.hostname.com/writes/

##### Sample response

```json
{
    "author": Author(),
    "book": Book()
}
```

</details>

<details><summary><b>Creditscards</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/creditscards/

##### Sample request

```json
{
    "owner": "",
    "flag": "",
    "number": "",
    "number_security": ""
}
```

[GET] http://www.hostname.com/creditscards/

##### Sample response

```json
{
    "owner": "",
    "flag": "",
    "number": "",
    "number_security": ""
}
```

</details>

<details><summary><b>Orders</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/orders/

##### Sample request

```json
{
    "client": Client(),
    "manager": Manager(),
    "status": Status(),
    "total": 0.0
}
```

[GET] http://www.hostname.com/orders/

##### Sample response

```json
{
    "client": Client(),
    "manager": Manager(),
    "status": Status(),
    "total": 0.0
}
```

</details>

<details><summary><b>Itemsorders</b></summary><blockquote>

#### Allowed methods = [GET, POST, PUT, PATCH, DELETE]

[POST] http://www.hostname.com/itemsorders/

##### Sample request

```json
{
    "book": Book(),
    "amount": 0,
    "subtotal": 0.0,
    "order": Order()
}
```

[GET] http://www.hostname.com/itemsorders/

##### Sample response

```json
{
    "book": Book(),
    "amount": 0,
    "subtotal": 0.0,
    "order": Order()
}
```

</details>

## License

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---