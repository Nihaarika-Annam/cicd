FROM openjdk:11

EXPOSE 8080

ADD target/devops-image.jar devops-image.jar

ENTRYPOINT ["java","-jar","/devops-image.jar"]

FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python", "manage.py", "runserver", "0:8000"]

