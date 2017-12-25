# Sample Java Webservice Running in Docker

A Sample java based rest service that can run independently and in docker container.
For the java docker file we can use the alpine linux based distribution.
https://hub.docker.com/_/openjdk/

## Getting Started

### Prerequisites

* Java 8
* Apache Maven 3.* or higher.
* Docker

### Executing and Running

In the command window go to project root directory test-cxf-boot

```
mvn clean package
java -jar target/test-cxf-boot.jar

```
Alternatively, you can also run  the jar by using below maven command.

```
mvn spring-boot:run
```

## Browse and test without docker

Go to the browser and open below URL, to see the JSON response
```
http://localhost:5000/services/helloCXF/json/aman
```

Go to the browser and open below URL, to see the XML response
```
http://localhost:5000/services/helloCXF/xml/aman
```
#### You should see json response greetings.

## Docker Commands
Build the docker image
```
docker build -t myservice .
```
Run the docker image
```
docker run -it -p 5000:5000 myservice:latest
```
Go to the browser and open below URL, to see the WADL
 ```
http://localhost:5000/services/helloCXF/json/aman
```

To Remove an image
```
docker rmi myservice
```
