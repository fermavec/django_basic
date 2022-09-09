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
We worked on the next files:
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
We worked on the next files:
* basicapp/models.py -> Two DB tables created by ORM using OOP
* /settings.py -> new parameter added in INSTALLED_APPS section
* Console -> command: py manage.py makemigrations "appname"
* Console -> command: py manage.py migrate

Migrations are an historical file that helps everyone to replicate 
the DB structure created

## Django Shell
Django has it's own shell to work and you can access by:
Command: py manage.py shell

Then run:
* from "modelname".models import "classname"
* "classname".objects.all() -> Brins all the info register in "classname"
* from django.utils import timezone -> helps us to create date time objects
* "variablename" = "classname"(atribute_1="data"...+) -> Registers new object
* "variablename".save() -> saves the variable in DB
* "variablename".attribute -> shows the attribute value

## Method GET
Allows you to get only one value of an object using some condition. 
Command: "Classname".objects.get("condition")
(a condition example can be: pk=# -> shows the data saved whit the primary key you selected)

## Method FILTER
This method let you to get more than one value. Is the same sintaxis as get method,
you just need to change "get" by "filter"
Example:
"Classname".objects.filter("date_atribute"__year= timezone.now().year) -> You'll get all the objects published at the year

## 3. Choices
To assign a value from some table to another one, you can use:

* "varname"."tableclass"_set.create("atributes") -> Creates a new object associated to "varname"
* "varname"."tableclass"_set.all() -> To view all the objects associated
* "varname"."tableclass"_set.count() -> To count all the objects associated

## Django Manager
It is a graphic interface that let us work with Django whitout code knowledge

ALERT!
To use the next command you should be carefull because it will contain sensitive information.
* py manage.py createsuperuser
* Set your username and password
* Enable the models you want in the manager in /admin.py file (admin.site.register("modelname"))
* Then go to hostpage/admin
* Type your username and password

## MTV (Model Template View) Architecture
Django let us build simple webapps. To do that, Django uses MTV to work the backend(Views)
and Front end (Templates). 

A view can be made by functions (function based view) or with classes (Generic View). To see the
code go to appbasic/views.py file

## 4. Index Template
We worked on the next files to create the first template for our webapp:
* polls/views.py
* polls/urls.py
* polls/templates/index.html

## 4. 404 Error
We worked on the next files:
* polls/views.py
* polls/templates/detail.py

## 5. Labels
We used Django labels to avoid hardcoding. Files updated:
* polls/urks.py
* /templates/polls/index.html

## 6. Forms
Worked on a form to submit. The files modified are:
* /templates/polls/detail.html

## 7. Vote View
We worked on the view for vote section. Files updated:
* polls/views.py

# Documentation
https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro