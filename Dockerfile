FROM python:3.11-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./ra_scraper ./ra_scraper
COPY ./launch ./launch
COPY ./main.py ./
COPY ./Makefile ./

ENTRYPOINT [ "python3", "main.py" ]
