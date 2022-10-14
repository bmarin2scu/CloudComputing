# CloudComputing_week3_lab

cd ..
cd dba

docker build -t my_dba .
docker run --name mydba --network mynetwork -p 8081:80 -d my_dba 

Localhost:8081
#admin@admin.com
#pass
Add Server: name/host mydb, user=root, password=pass, 

cd ..

docker build -t my_django .
docker run -it -p8000:8000 -v $(pwd):/app my_django /bin/bash
django-admin startproject mysite
Exit
docker run -it -p8000:8000 --network mynetwork -v $(pwd)/mysite:/app my_django /bin/bash
python manage.py migrate
python manage.py createsuperuser
#user=root
#email=a@a.com
#password=pass

#connect postpre in settings.py file
## settings.py file 
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'mydb',
        'PORT': 5432,
  ##  }
##}

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
Localhost:8081
#updates to tables 
