FROM openjdk:11

WORKDIR /app

COPY /javaoop /app

RUN javac Main.java

CMD ["java","Main"]