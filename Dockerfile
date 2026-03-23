FROM python:3.15.0a7-alpine3.22

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD [ "python","app.py" ]