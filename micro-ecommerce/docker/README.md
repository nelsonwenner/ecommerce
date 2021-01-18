<h1 align="center"> Docker Scripts </h1>

## :thinking: What's the point?
* Setting up the devjobs app on your local machine is quick and easy with the aid of Docker and Docker Compose.
* Docker provides a common virtual environment available to all developers and resolves the infamous "but it works on my machine" problem.
* Use the scripts in this directory to execute tasks in Docker.  Please note that these scripts are intended to be executed from this app's root directory.  These scripts allow you to bypass the need to keep typing "docker-compose run rails-app".

## :whale2: Installing Docker
* You should have at least 2 GB free on your local machine to download Docker images and create Docker containers for this app.
* Docker installation instructions are at https://docs.docker.com/install/.
* Docker Compose installation instructions are at https://docs.docker.com/compose/install/.
* To run Docker commands as a regular user instead of as root (with sudo), follow the instructions at https://docs.docker.com/engine/install/linux-postinstall/.

## :information_source: Getting Started
* Open a terminal with a shell.
* Clone the repository. Begin by forking this repo with the Fork button in the top-right corner of this screen.
* Use git clone to copy your fork onto your local machine.
```sh
$ git clone https://github.com/YOUR_GITHUB_USERNAME_HERE/ecommerce
```
* Go at the root of the app:
```sh
$ cd micro-ecommerce
```
* Download the Docker images, build the Docker containers, AND log the screen output from these tasks:
```sh
$ docker/build
```
* Run the server and its required Docker containers:

```sh
$ docker/server
```
* The default admin user is 'admin@user.com' with the password '123456'.
* View the app in the browser at `http://localhost:8000/admin`.
* You will then get the trace of the containers in the terminal. You can stop the containers using Ctrl-C in the terminal.

## :page_with_curl:	Script Summary
* docker/build: This script builds the Docker containers specified for this app, and logs the screen output for these operations.  After you use "git clone" to download this repository, run the docker/build script to start the setup process.
* docker/server: Use this script to run this app in the Rails server.  This script executes the "docker-compose up" command and logs the results.  If all goes well, you will be able to view this app on your local browser at http://localhost:8000/.
* docker/test: Use this script to run the entire test suite.
* docker/run: Use this script to run commands within the Docker container.  If you want shell access, enter "docker/run bash".  To execute "ls -l" within the Docker container, enter "docker/run ls -l".
* docker/kill: This script destroys all Docker containers but leaves the Docker images alone. 
