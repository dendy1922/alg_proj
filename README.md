## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Commands](#commands)
* [Creating files socket and service files for Gunicorn](#creating-files-socket-and-service-files-for-gunicorn)
* [Configure Nginx to Proxy Pass to Gunicorn](#configure-nginx-to-proxy-pass-to-gunicorn)


## General info
This project is test task project


## Technologies
Project is created with:
* Python: 3+
* Django version: 3.0
* Postgresql
* psycopg2-binary
* gunicorn
* nginx
* venv


## Commands
Clone project:

    $ git clone https://github.com/dendy1922/alg_proj


To run server on localhost:
    
    python manage.py runserver 0.0.0.0:8000

Path of the project:
    
    mkdir ~/myprojectdir
    cd ~/myprojectdir
    
Creating Virtualenv and using:

    virtualenv myprojectenv
    pip install django gunicorn psycopg2-binary
    
Creating project: 

    django-admin.py startproject myproject ~/myprojectdir
    
###For working you need to Create instances in django admin in Algorithm_description:
    
     name = Bubble
     name = Merge
     name = Insertion

For adding different algoritms you have to append name of algorithm in model Algorithm_description
write class with method realize in utils.py  and connect class and name in simple_dict in utils.py

## Creating files socket and service files for Gunicorn

Open socket file with redactor:
    
    sudo nano /etc/systemd/system/gunicorn.socket

Change file:
    
    [Unit]
    Description=gunicorn socket
    
    [Socket]
    ListenStream=/run/gunicorn.sock
    
    [Install]
    WantedBy=sockets.target

Close socket file.

Open service file with redactor:

    sudo nano /etc/systemd/system/gunicorn.service
    
Change file:

    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target
    
    [Service]
    User=tim
    WorkingDirectory=/home/tim/python/myprojectdir
    ExecStart=/home/tim/python/django/myprojectdir/myprojectenv/venv/bin/gunicorn \
              --access-logfile - \
              --workers 3 \
              --bind unix:/run/gunicorn.sock \
              myproject.wsgi:application

    [Install]
    WantedBy=multi-user.target
    
Save and close the file. 
Then, start Gunicorn service and enable it to start on boot time with the following command:
   
    systemctl start gunicorn
    systemctl enable gunicorn

##Configure Nginx to Proxy Pass to Gunicorn

Create and fill file:

    server {
    listen 80;
    server_name server_server;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/tim/myprojectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
    }
    
Save file. Enable the Nginx virtual host by creating symlink.

    sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
   
Restart Nginx by running the following command:

    systemctl restart nginx
    
Now, Nginx is configured to pass the traffic to the process.





