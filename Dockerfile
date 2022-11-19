# syntax=docker/dockerfile:1

FROM python:3.10-slim

WORKDIR /book_search

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]