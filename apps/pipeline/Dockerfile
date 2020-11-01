FROM python:3.8

RUN pip install --upgrade pip

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY wait /wait
RUN chmod +x /wait

COPY app /app

ENV PYTHONPATH="${PYTHONPATH}:/app"
WORKDIR /app