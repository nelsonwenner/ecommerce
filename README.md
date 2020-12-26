<h1 align="center">
  System E-commerce
</h1>

<p align="center">
  
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/nelsonwenner/ecommerce?color=%2304D361">

  <a href="https://github.com/nelsonwenner">
    <img alt="Made by @nelsonwenner" src="https://img.shields.io/badge/made%20by-%40nelsonwenner-%2304D361">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361">

  <a href="https://github.com/nelsonwenner/ecommerce/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/nelsonwenner/ecommerce?style=social">
  </a>
</p>

<p align="center">
  <a href="#technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

## :bulb: About the project
#### The application was built using the concepts of microservices and architected with Docker.

## :telescope: System architecture
<div align="center">
  <img alt="system-architecture" src="./screens/system-ecommerce.png" />
</div>

## :rocket: Technologies
* [Docker](https://www.docker.com/)
* [DockerCompose](https://docs.docker.com/compose/)
* [PostgreSql](https://www.postgresql.org/)
* [Django](https://www.djangoproject.com/)
* [Celery](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
* [Node](https://nodejs.org/en/)
* [ReactJS](https://reactjs.org/)
* [RabbitMQ](https://www.cloudamqp.com/)

## :electric_plug: Prerequisites
* Docker Compose version (>= 1.25.x)
* Docker version (>= 19.03.x)
* PostgreSql (>= 9.x)
* Node version (>= 12.18.x)
* Npm version (>= 6.14.x)
* Python (>= 3.x)

## :information_source: Getting Started
  1. Fork this repository and clone it on your machine.
  2. Change the directory to ecommerce where you cloned it.
  
## :closed_lock_with_key: Backend Getting Started 

```shell
/* After clone this repo, enter in the micro-ecommerce-api folder */
$ docker-compose up
```

## :computer: Web Application Getting Started

```shell
/* After clone this repo, enter in the Web folder */
$ cd frontend

/* Create `.env` of the system */
$ cp .env.example .env

/* Install dependencies */
$ npm install

/* Run the project */
$ npm start
```
  * Certify yourself that the backend is running on [localhost:8000](http://localhost:8000), Open frontend, the host [localhost:3000](http://localhost:3000) 

## :memo: License
This project is under the MIT license. See the [LICENSE](LICENSE.md) for more information.

---