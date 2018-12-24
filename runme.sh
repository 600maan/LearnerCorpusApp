  #!/bin/bash
 
 echo "Install required Tools"
 apt-get update
 apt-get -y upgrade
 apt-get install -y python3.7
 apt install -y python3-pip
 pip3 install -r requirements.txt --user 
 
 echo "Start Server"
 python3 manage.py runserver localhost:80
 
