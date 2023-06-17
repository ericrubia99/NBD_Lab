# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV n_packets 10

RUN wget -o data/${n_packets}_packets.pcap https://nbd-lab.s3.amazonaws.com/${n_packets}_packets.pcap

ENV type ""
ENV output_dir "./"
ENV file "./data/packets.pcap"

CMD ["sh", "-c", "python3 read.py -${type} -f=${file} -o=${output_dir}"]