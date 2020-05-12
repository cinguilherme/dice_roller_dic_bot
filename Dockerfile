FROM python:3.8

RUN python3 -m pip install -U discord.py flake8 pytest coverage pytest-cov

COPY . /app

WORKDIR /app
