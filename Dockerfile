FROM python:3.8

COPY . /app

WORKDIR /app

RUN python3 -m pip install -U discord.py

RUN pip install -r requirements.txt