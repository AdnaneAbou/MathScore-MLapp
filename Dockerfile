FROM python:3.9
WORKDIR /app
COPY . /app

RUN apt update -y 

RUN apt install -y build-essential

RUN pip install -r requirements.txt

CMD [ "python","app.py" ]