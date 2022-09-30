#use python version 3.8.13, to conserve compatability for future use 
FROM python:3.8.13-bullseye AS willynilly

#if you do not specify user, runs everything as root. If someone gets access to root then has access to whole system 
## some parts of install may still need to be run as root in order to have access to install 
ENV USER=cloudy

#docker build -t my_jupyter .
#docker run -it my_jupyter