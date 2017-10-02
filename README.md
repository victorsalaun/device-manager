# Device Manager

Very simple Django based app using  Django Rest Framework

##Prerequisites

* python  3
* pip

## Installation

    pip install -r requirements.txt

## Init

    python manage.py migrate

In order to create admin user:

    python manager.py createsuperuser

## Launch

    python manage.py runserver
    
[Admin page](http://127.0.0.1:8000/admin/)

[Api page](http://127.0.0.1:8000/api/devices/)