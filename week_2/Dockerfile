
## build and run commands
#docker build -t my_jupyter .
#docker run -it my_jupyter

#use python version 3.8.13, to conserve compatability for future use 
FROM python:3.8.13-bullseye AS willynilly

#if you do not specify user, runs everything as root. If someone gets access to root then has access to whole system 
## some parts of install may still need to be run as root in order to have access to install 
USER root

#install jupyter, can also use from terminal
RUN pip3 install jupyter

# docker run -p 7777:7777 my_jupyter

## source: https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f

#2 ways to create user
## RUN useradd -ms /bin/bash our_user
#ENV USER=name
ENV JUPYTER_USER our_user

RUN useradd -ms bin/bash ${JUPYTER_USER} \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $JUPYTER_USER ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$JUPYTER_USER \
    && chmod 0440 /etc/sudoers.d/$JUPYTER_USER

RUN mkdir -p home/our_user/week2lab
#expose port 
EXPOSE 7777

USER ${JUPYTER_USER}
#run jupyter notebook on specific port, allow-root should not be used in actual running system 

CMD jupyter notebook --ip=0.0.0.0 --port 7777

