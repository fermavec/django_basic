# Django Basics

Using VSCode, CMder, Django, Git Bash and Google Chrome

## First interaction with Django.

Install in virtual environment:
pip install django

Running Django:
django-admin startproject "appname"

## Explaining the created files

* namedirectory/ Django can't manage this directory
* /manage.py  Code wich has commands that we are gonna use in Django
* namedirectory/namedirectory/ Django project directory (Django can manage it)
* namedirectory/namedirectory/__init__.py Indicates that this directory is a package
* namedirectory/namedirectory/asgi.py File that help us to deploy
* namedirectory/namedirectory/wsgi.py File that also help us to deploy
* namedirectory/namedirectory/settings.py Contains all the project configuration info
* namedirectory/namedirectory/urls.py Contains the project urls that we are using

## Development Server
Allows us to run a software server were we can make changes before production

Command:
(Move to directory and run) 
py manage.py runserver

* Remember: in settings.py there is a variable called DEBUG. When you
are working localhost it has to be TRUE; if you upload your project to 
production, the variable DEBUG has to be FALSE.

## Projects vs Apps
In Django we work by project but, every project can have many apps.

To create an app enter the next command:
py manage.py startapp "appname"

## 1. Hello Fer Mavec
We work on the next files:
* /polls/views.py -> HttpResponse imported,  index function created
* /polls/urls.py -> Libraries imported and urlpattern list created
* /urls.py -> "include" was imported and new pattern registered

### ORM (Object Relational Mapping)
Using some libraries and frameworks I can simulate and relate a RDB 
(Relational DataBase) through OOP (Object Oriented Programming) paradigm. In
Django, each table from database will be represented as model (an OOP class);
each column from RDB will be created as an attribute for that class and each
datatype will be a nested class.

## 2. ORM and Migrations
We work on the next files:
* basicapp/models.py -> Two DB tables created by ORM using OOP
* /settings -> new parameter added in INSTALLED_APPS section
* Console -> command: py manage.py makemigrations "appname"
* Console -> command: py manage.py migrate

Migrations are an historical file that helps everyone to replicate 
the DB structure created