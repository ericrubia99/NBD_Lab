# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN  apt-get update -y && \
     apt-get install unzip

RUN unzip -o data/packets.zip -d data/


ENV type ""
ENV output_dir "./"
ENV file "./data/packets.pcap"

CMD ["sh", "-c", "python3 read.py -${type} -f=${file} -o=${output_dir}"]