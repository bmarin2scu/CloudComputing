FROM postgres:12.12
#generic credentials for class purposes
ENV POSTGRES_USER='root'
ENV POSTGRES_PASSWORD='pass'
ENV POSTGRES_DB='web'
EXPOSE 5432
#pwd command shows you current path in terminal 
#docker build -t my_db .
#-itd runs as interactive demon(background)
##docker run --name mydb -itd -p5432:5432 my_db

#need to connect db and dba containers, create with network 
##docker network create mynetwork, network stays
###docker network ls
# docker run --name mydb2 --network mynetwork -p 5432:5432 -d my_db