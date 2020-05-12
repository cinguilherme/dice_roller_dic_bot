FROM python:3.8

RUN python3 -m pip install -U discord.py

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt