## Django Basics

# First interaction with Django.

Install in virtual environment:
pip install django

Run Django:
django-admin startproject "appname"

# Explaining the created files

namedirectory/ Django can't manage this directory
/manage.py  Code wich has commands that we are gonna use in Django
namedirectory/namedirectory/ Django project directory (Django can manage it)
namedirectory/namedirectory/__init__.py Indicates that this directory is a package
namedirectory/namedirectory/asgi.py File that help us to deploy
namedirectory/namedirectory/wsgi.py File that also help us to deploy
namedirectory/namedirectory/settings.py Contains all the project configuration info
namedirectory/namedirectory/urls.py Contains the project urls that we are using