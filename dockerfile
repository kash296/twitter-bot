#Dockerfile to deploy Kaushik Murali's twitterbot
FROM ubuntu:20.04
LABEL maintainer="mkaushik1124@gmail.com"
LABEL description="A Python Twitter Bot that tweets information about the current day"

#Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

#Copy Source Files to container
COPY botsrc /botsrc

#Commands to Install packages 
RUN apt update && apt install -y python3 python3-pip
RUN pip3 install tweepy wikipedia

#Run the bot to finish deployment
RUN python3 /botsrc/twitbot.py


