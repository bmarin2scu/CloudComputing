FROM dpage/pgadmin4:6.14
#do not use in prod or github, exposes username and password 
##This is for class purpose, or else need to set up system to manage users/passwords
ENV PGADMIN_DEFAULT_EMAIL=admin@admin.com
ENV PGADMIN_DEFAULT_PASSWORD=pass
EXPOSE 80
## pgAdmin may take a few minutes to start up and load

#docker run --name mydba --network mynetwork -p 8081:80 -d my_dba 
# -p ports
# -v volume
# -e env