#best to specify version when building files, current python is 3.10.7
FROM python:latest AS build
RUN apt-get update
RUN apt-get install wget

#use run to create file, pull from github
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
#alternative method: ADD https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv fb_sub.csv

#find combinations of regex to find company name
## name output file company.txt
RUN awk -F',' 'FNR==2{print $3}' fb_sub.csv >> company.txt
### source: https://www.gnu.org/software/gawk/manual/html_node/Regexp-Usage.html

# run docker container from image
#docker run --restart=always -p 8888:80 company
##source: https://phoenixnap.com/kb/docker-run-command-with-examples

##bonus points if able to access file in container

### dockps
###>>find container ID

### docker cp [container_ID]:company.txt ~/Desktop/GradSchool/Fall2022/CloudComputing/GitHub/CloudComputing/week_1/company.txt
###>> create copy of company.txt file to github clone

#### above comands allow user to run container, access container ID and copy txt file to local GitHub cloned repository
##alternate source for copying containter files: https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-copy-files-from-a-Docker-container-to-a-host-machine#:~:text=Obtain%20the%20name%20or%20id,the%20file%20on%20the%20host
