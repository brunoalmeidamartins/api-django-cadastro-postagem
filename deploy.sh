#!/bin/bash
PATH_BASE='/app/django_rest'
sleep 30 #Tempo para subir o banco de dados
python $PATH_BASE/manage.py makemigrations
python $PATH_BASE/manage.py migrate
python $PATH_BASE/manage.py runserver 0.0.0.0:8000 #Roda a aplicação