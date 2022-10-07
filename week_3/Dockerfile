FROM python:latest 

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

VOLUME /app
WORKDIR /app

EXPOSE 8000

# docker build -t my_django .
# docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash
# django-admin startproject mysite ;in terminal /bin/bash from my_django 
##not in dockerfile, do not want to build/restart everytime container is run 
# python manage.py migrate to finish installing django


### python /app/app/manage.py createsuperuser
#user=root
#email=a@a.com
#password=pass

#connect postpre
## settings.py file 
## DATABASES = {
  ##  'default': {
  ##      'ENGINE': 'django.db.backends.postgressql',
  ##        'NAME': 'web',
  ##        'USER': 'root',
  ##        'PASSWORD': 'pass',
  ##        'HOST': 'my_db',
  ##        'PORT': 5432,
  ##  }
##}

#python manage.py runserver 0.0.0.0:8000
#python manage.py migrate
# docker run -it -p8000:8000 --network mynetwork -v $(pwd)/app:/app my_django /bin/bash