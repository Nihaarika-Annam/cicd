FROM openjdk:11

EXPOSE 8080

RUN yum install -y git

COPY . /app

ADD target/devops-image.jar devops-image.jar

ENTRYPOINT ["java","-jar","/devops-image.jar"]


