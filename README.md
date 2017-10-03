# Device Manager

Very simple Django based app using  Django Rest Framework

##Prerequisites

* python  3
* pip

## Installation

    pip install -r requirements.txt

## Init

**Keycloak**

Set Keycloak realm 'django':

* Client ID: device_manager
* Root URL: http://localhost:8000
* Valid Redirect URIs: /openid/callback/*
* Web Origins: *


    py manage.py makemigrations bossoidc

    python manage.py migrate

## Launch

    python manage.py runserver
    
[Admin page](http://127.0.0.1:8000/admin/)

[Api page](http://127.0.0.1:8000/api/devices/)

[Main page](http://127.0.0.1:8000/)