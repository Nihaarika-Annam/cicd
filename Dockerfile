python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python", "manage.py", "runserver", "0:8000"]
