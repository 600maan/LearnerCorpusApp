HOST=0.0.0.0
PORT=80

install_python:
  sudo apt-get update
  sudo apt-get -y upgrade
  sudo apt-get install -y python3.7
  sudo apt install -y python3-pip
  pip install -r requirements.txt --user 
  
run:
  python manage.py runserver $(HOST):$(PORT)

