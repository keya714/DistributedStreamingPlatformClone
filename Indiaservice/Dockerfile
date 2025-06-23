FROM python:3.12.6

WORKDIR /app

COPY . /app

RUN pip install flask

RUN pip install requests

EXPOSE 8050

CMD python ./App.py