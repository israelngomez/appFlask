
FROM python:3.9.16-alpine3.16

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python3", "./app.py"]