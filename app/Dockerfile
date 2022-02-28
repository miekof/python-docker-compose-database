# syntax=docker/dockerfile:1
FROM python:3.7-slim
WORKDIR /app
RUN apt-get update && apt-get install
RUN apt-get install -y --no-install-recommends gcc bash libmariadb3 libmariadb-dev 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
