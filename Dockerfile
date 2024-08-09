FROM openjdk:11

EXPOSE 8080

FROM docker.io/library/openjdk:11

RUN apt-get update && apt-get install -y git

COPY . /app

ENTRYPOINT ["java","-jar","/devops-image.jar"]


