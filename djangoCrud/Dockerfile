FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

WORKDIR /myApp

COPY requirements.txt /myApp

RUN pip3 install -r requirements.txt

COPY . /myApp

EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
