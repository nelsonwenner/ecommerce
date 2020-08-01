<h1 align="center">Ecommerce - API REST</h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/nelsonwenner/django-ecommerce-api?color=%2304D361">

  <a href="https://github.com/nelsonwenner">
    <img alt="Made by @nelsonwenner" src="https://img.shields.io/badge/made%20by-%40nelsonwenner-%2304D361">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361">

  <a href="https://github.com/nelsonwenner/ecoleta/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/nelsonwenner/django-ecommerce-api?style=social">
  </a>
</p>

<div align="center">
  <img alt="dashboard" src="./screens/dashboard.png" />
</div>

## :rocket: Technologies

* [Django rest framework](https://www.django-rest-framework.org/)
* [Django](https://www.djangoproject.com/)

## :electric_plug: Prerequisites

- [Python3 (>= 3.x)](https://www.python.org/downloads/)

## :closed_lock_with_key: Getting Started

1. Fork this repository and clone it on your machine.
2. Change the directory to `django-ecommerce-api` where you cloned it.

```shell
/* Install Virtualenv */
$ pip install virtualenv

/* Creating the project env */
$ virtualenv env

/* Using the project env */
$ source env/bin/activate

/* Installing dependencies */
$ pip install -r requirements.txt

/* Run the migrations */
$ python3 manage.py migrate

/* Run the fake data */
$ python3 manage.py loaddata fake_data

/* Run the initial data */
$ python3 manage.py loaddata initial_data

/* Run server /*
$ python3 manage.py runserver
```

## :telescope: Diagram Database

<p align="center">
  <img alt="diagram" src="./screens/diagram.png" />
</p>

## :shield: Admin Access dashboard

```
Email: admin@user.com
Password: 123456
```
  * Open the host [localhost:8000/admin](http://localhost:8000/admin) 

## :memo: License
This project is under the MIT license. See the [LICENSE](LICENSE.md) for more information.

---
