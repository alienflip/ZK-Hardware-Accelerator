FROM ubuntu:18.04

RUN apt-get -qq update && \
    apt-get -qq upgrade && \
    apt-get -y install build-essential software-properties-common python python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

COPY . /mnt

CMD ["bash", "./mnt/initRun.sh"]