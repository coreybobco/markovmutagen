FROM python:3.6.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt --src /usr/local/src

ENTRYPOINT python3 server.py