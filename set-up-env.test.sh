#!/bin/bash

# DB
echo "MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD" >> .env
echo "MYSQL_USER=$MYSQL_USER" >> .env
echo "MYSQL_PASSWORD=$MYSQL_PASSWORD" >> .env
echo "MYSQL_DATABASE=$MYSQL_DATABASE" >> .env

# Django
echo "SECRET_KEY=$SECRET_KEY" >> .env
echo "DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS" >> .env
echo "DEBUG=$DEBUG" >> .env

