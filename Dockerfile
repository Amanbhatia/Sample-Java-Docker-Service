FROM openjdk:8
EXPOSE 5000
COPY target/test-cxf-boot.jar /usr
WORKDIR /usr
CMD java -jar test-cxf-boot.jar
