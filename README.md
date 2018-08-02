una ves descargado el virtualenv, se debe crear un ambiente virtual 

crear ambiente virtual:
virtualenv -p /usr/bin/python2.7 venv

activar virtualenv:
source venv/bin/activate

instalar django y paquetes necesarios en ambiente virtual:
//se deve tener activado el ambiente virtual para que los paquetes se intalen en el ambiente//
pip install Django

pip install djangorestframework

pip install markdown

pip install django-filter


luedo de correr el ambiente virtual  se ingresa a la carpeta dende esta el archivo manage.py ejemplo: cd /Users/macbookpro/papinotas/prueba_papinota/papinotas

se corre el servidor con el comando:
python manage.py runserver

para visualisar se ingresa al navegador la ruta: http://localhost:8000/GetGroups/?authentication_token=123 o http://localhost:8000/GetStudents/?authentication_token=123



Problema 1

una ves activado el ambiente virtual se ingresa a la carpeta dende esta el archivo manage.py ejemplo: cd /Users/macbookpro/papinotas/prueba_papinota/papinotas

se corre el servidor con el comando: 
python manage.py shell

luego se inporta ejercicio1:
from ejercicio1 import *

se copya el array de 100 numero que se encuentra en el ejercicio1.py para dejar numero que no existan en el arreglo se le asigna 0 

luego se llama a la funcion:
NumeroFaltante(array)

fin ...  
