# chatbot-api

<p align="center">
  <strong>ChatBot POC using available text2text APIs</strong>
</p>

# Technical context
Proposing a POC that will later serve


# Project tooling

- **OS**: Ubuntu 22.04
- **Platform**: Python
- **Framework**: [FastAPI](https://www.django-rest-framework.org)
- **Testing**: PyTest, Robot, [Behave](https://www.django-rest-framework.org)
- **Databases**: PostGreSQL (Relational), MongoDB(NoSQL), WeAviate/QDrant (Vector)
- **Migrations**: Fly or Liquibase
- **Dependecy Injection**: [Dependency Injector](https://python-dependency-injector.ets-labs.org/)
- **Containeurization**: Docker/Compose, Kubernetes
- **API**: Swagger 3
- **Logging**: [Tutorial](https://www.toptal.com/python/in-depth-python-logging)
- **DevOps**: Docker, K8s, Jenkins
- **Auth**: https://fastapi-contrib.readthedocs.io/en/latest/_modules/fastapi_contrib/auth/backends.html#AuthBackend.authenticate
- **Data dalidation, Serialization**: [Serialization with Pydantic](https://www.pedaldrivenprogramming.com/2020/12/fastapi-fundamentals-pydantic/)


# Setting up tools

## Install Python3 and create a virtual execution environment

You can follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-22-04-server)

NB: It is strongly recommended to work inside virtual environment

## Install FastAPI Framework and dependencies
(Make sure you are in your active venv)
In the root folder of the project hit the following command:

```bash
pip install -r requirements.txt
```

## Test your installation

In the project root folder, run:

**- Run the server**
```bash
uvicorn main:app --reload
```
Open on your web browser: http://127.0.0.1:8000

**- See the Swagger documentation**
At: http://127.0.0.1:8000/docs
Or: http://127.0.0.1:8000/redoc

## Design

### Modules
The Chatbot API code is organized around [feature modules](https://docs.nestjs.com/modules).
All the application's modules are found in the folder `./src/modules`.
To create a modules type the command: `nest g module modules/module-name`
Then manually create the module's folders hierarchy as follow:

<pre>
├──module-name
|  |
|  ├──domain
|  |  |
|  |  ├──models
|  |  |  |
|  |  |  ├──`{model_name}`.py
|  |  |  ├── ...
|  |  |  
|  |  ├──dto
|  |     |
|  |     ├── src `{transfer_operation_name}`_dto.py
|  |     ├── src ...
|  |   
|  ├──repository
|  |  |
|  |  ├──`{repository_name}`_repository.py
|  |  ├── ...
|  |
|  ├──services
|  |  |
|  |  ├──`{service_name}`_service.py
|  |  ├── ...
|  |  
|  ├──controllers
|  |  |
|  |  ├──`{controller_name}`_controller.py
|  |  |
|  |
|  ├── __init__.py
|     (module bootstrap for aggregating all the module's artifacts)
</pre>


Project structure is as follows:

<pre>
chatbot-api
|
├──config
|   ├──all configs files (db, services)
|
├──app
|  |
|  ├──modules
|  |  |
|  |  ├──`module 1`
|  |  |   {module 1 structure here: domain, repository, services, controllers + __init__.py}
|  |  |
|  |  ├──`module 2`
|  |  |   {module 2 structure here: domain, repository, services, controllers + __init__.py}
|  |  |
|  |  ├──`module n`
|  |
|  |
|  ├──core
|  |  |
|  |  ├── non business components: di, base components (Repo, Services, Exceptions), etc.
|  |  |__init__.py
|  |
|  |
|  ├── __init__.py
|  |   (Aggregating all the app ressources: module bootstraps, configs, core components)
|  |
|  ├── __init__.py
|      (bootstrap the application and launch the server)
|
|
├──tests
|  ├──unit
|  ├──functional
|  ├──integration
|  ├──acceptance
|  
|
├──all app utility files: .envs, git files, , etc.
|
├──devops
|  (devops related files)
|
|
|
</pre>

#### Domain Driven Design
As this is meant to be a Data-Intensive application that will need to access various types of datasources
(In-memory, SQL, NoSQL Documents, Vector) it is important right from the begining to opt for a Domain Driven Design.

This means that we will massively make use of the Repository Pattern, Service Layer and Unit Of Work.
Each module will be based ...
- Data validation: [Django RF Validators](https://www.django-rest-framework.org/api-guide/validators/), [Pydantic](https://docs.pydantic.dev/latest/),


#### Code design practices and recommendations
- Follow the [12 factor app](https://12factor.net) principles
- Use 4 spaces for indentation

## Tools integration


### FastAPI
https://fastapi.tiangolo.com/
FastAPI is the most suitable python framework for AI apps and any application that is built with
performance and scalability in mind and may suit for data-intensive processing app; 

### MongoDB
We use motor+pymongo; motor provides MongoDB asynchronous requests capabilities
https://github.com/mongodb-developer/mongodb-with-fastapi

## Security
- [Auth](https://fastapi.tiangolo.com/tutorial/security/first-steps/)

# Tasks
[Celery](https://testdriven.io/courses/fastapi-celery/)

# Testing
This section shows how to install and use testing tools

## Installation

### Installation of Robot
Checkout doc [Robot](https://www.django-rest-framework.org)

### Installation of Behave
Checkout doc [Behave](https://www.django-rest-framework.org)

### Installation of PyTest
Checkout doc [PyTest](https://www.django-rest-framework.org)

## Test Design

Tests are organized in three components: unit test, functional tests, integretion tests and acceptance tests
Some used Testing patterns are [Unit of Work Patterns](https://www.cosmicpython.com/book/appendix_django.html)

## Running tests

### Unit tests

### Functional tests

### Acceptance tests


## License

Nest is [MIT licensed](LICENSE).

