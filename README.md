# Mozio
Backend Python Coding Project

# API Docs

> ~~BaseURL : http://ec2-13-232-249-114.ap-south-1.compute.amazonaws.com/~~ (Terminated Due to Billing Constraint)
                      Will be migrating to [Heroku](http://heroku.com) or [Deta](http://deta.sh) in the future.

```
Endpoints : 
  - /providers/
  - /service-areas/
```
[BrowsableAPIRenderer Docs From DjangoRestFramework](http://ec2-13-232-249-114.ap-south-1.compute.amazonaws.com/) 


[Swagger Docs](http://ec2-13-232-249-114.ap-south-1.compute.amazonaws.com/docs) 

[Postman Documentation : Detailed Docs](https://documenter.getpostman.com/view/16147280/Tzz7Nxz4) 



## Docker Command to run PostGIS Image: 

>``sudo docker run --name "postgis" -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -d -t kartoza/postgis``

## Commands to run inside Docker Container : 
```
- docker exec -it pg_container bash #To get inside the docker container
- \l # To check databases in Postgres
- create database mozio; # To create new database named mozio
```

## Steps to run Development Server :
```
Make venv : python3 -m venv env-mozio

source env-mozio/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py test

python manage.py collectstatic

python manage.py runserver 0.0.0.0:80
```

## Server Setup (Ubuntu 18.04):
```
copy gunicorn.socket to /etc/systemd/system/gunicorn.socket
copy gunicorn.service to /etc/systemd/system/gunicorn.service

Use Commands:
- sudo systemctl start gunicorn.socket
- sudo systemctl start gunicorn
- sudo systemctl enable gunicorn.socket
- sudo systemctl enable gunicorn

Check if is gunicorn running : 
- curl --unix-socket /run/gunicorn.socket localhost

Rename nginx_moziotask to moziotask

- copy moziotask to /etc/nginx/sites-available/moziotask

##Create symlink moziotask to sites-available
- sudo ln -s /etc/nginx/sites-available/moziotask /etc/nginx/sites-enabled 

- Update nginx.conf at /etc/nginx/nginx.conf

## If Deploying on a Domain (Currently i'm using EC2 without any domain so according to the policy of certbot its Forbidden)
  - sudo snap install --classic certbot
  - sudo ln -s /snap/bin/certbot /usr/bin/certbot
  - sudo certbot --nginx
```

## Infra & Tools used for Deployment :
```
  - AWS EC2 (t2.micro)
  - Python3.6.9
  - Gunicorn
  - Docker
  - PostGIS running on Docker
  - Nginx
```

## Scope for future development :

```
  - Authentication using JWT or TokenAuth
  - SSL
  - Hosting PostGIS on AWS RDS
  - Creating AutoScaling Group on AWS 
    - Attaching a Elastic Load Balancer for inbound requests.
  - Using Redis for Caching
    - Hosting it on AWS Elasticache so that all EC2 can connect to same   
      Redis.
  - Rate Limiting API using Redis (INCR) & (EXPIRE) on the User-Keys.
