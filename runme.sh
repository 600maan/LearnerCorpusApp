  #!/bin/bash
 
 echo "Install Python 3.7 and required dependencies"
 apt-get update
 apt-get -y upgrade
 apt-get install -y python3.7
 apt install -y python3-pip
 pip3 install -r requirements.txt --user 
 
 echo "Install MongoDB"
 apt-get install -y mongodb
 
 
 echo "Start Python Application"
 python3 manage.py runserver localhost:80
 
