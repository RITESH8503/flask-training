### Deployment to cloud

#### 1. Intsall and configure virtual environment

#### 2. `pip install gunicorn`

#### 3. Create and run Gunicorn service

`sudo vim /etc/systemd/system/gunicorn.service`

Add the following lines

    [Unit]
    Description=gunicorn daemon
    After=network.target

    [Service]
    User=www-data
    Group=www-data
    WorkingDirectory=/var/www/pyapp/

    ExecStart=/usr/local/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/pyapp.sock wsgi:app

    [Install]
    WantedBy=multi-user.target

Start the service

  `sudo systemctl start gunicorn`

  `sudo systemctl enable gunicorn`

#### 4. Configure Nginx

    `sudo vim /etc/nginx/sites-available/mysite.com`

    server {
    listen 80;
    server_name your_domain.com www.your_domain.com;

        location / {
            include proxy_params;
            proxy_pass http://unix:/var/www/pyapp/pyapp.sock;
        }
    }

    cd /etc/nginx/sites-enabled
    sudo ln -s ../sites-available/mysite.com .
    sudo service nginx restart