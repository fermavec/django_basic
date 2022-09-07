# Django Basics

Using VSCode, CMder, Django, Git Bash and Google Chrome

## First interaction with Django.

Install in virtual environment:
pip install django

Run Django:
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