FROM python:3.9.13-alpine3.16

RUN apk add make automake gcc g++ subversion python3-dev

RUN pip install --upgrade pip

ADD . /Flask_Login

WORKDIR /Flask_Login

RUN pip install -r requirements.txt

CMD python app.py
