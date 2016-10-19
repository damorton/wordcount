FROM python:2.7.11-onbuild
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libboost-all-dev
    
RUN cd wordcount && rm -rf build/ && ./buildunix.sh

EXPOSE 27002
