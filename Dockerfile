# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN  apt-get update \
  && apt-get install -y wget

ARG n_packets

RUN wget https://nbd-lab.s3.amazonaws.com/${n_packets}_packets.pcap -P data/

ARG type
ARG output_dir

ENV output_dir=${output_dir}
ENV type=${type}
ENV file=data/${n_packets}_packets.pcap

CMD ["sh", "-c", "python3 read.py -${type} -f=${file} -o=${output_dir}"]