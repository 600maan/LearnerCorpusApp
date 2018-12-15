# LearnerCorpusApp
A Django web application for language learner Corpus



Install python and pip in Ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart

Install Django in Ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04

Install latest Django to use path library

pip3 install --upgrade django

Dependencies
1) python 3.7.0
2) pip install nltk
3) pip install djangorestframework
4) pip install django-cors-headers

Notes
1) Add return concordance_list to the print_concordance function in nltk.text.py


Start Server
80 : default HTTP port
python manage.py runserver 0.0.0.0:80


Kill Process on ubuntu

https://stackoverflow.com/questions/9346211/how-to-kill-a-process-on-a-port-on-ubuntu
