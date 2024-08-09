FROM openjdk:11

EXPOSE 8080

RUN yum install -y git

COPY . /app

ENTRYPOINT ["java","-jar","/devops-image.jar"]


