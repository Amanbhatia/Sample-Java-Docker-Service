package com.mycompany.rest.service.impl;
import com.mycompany.rest.service.HelloCXF;

public class HelloCXFImpl implements HelloCXF {
 
    public String sayHelloJson(String name) {
        return "Hello " + name + ", Congrat! You created Spring Boot CXF Json API!!!";
    }

    public String sayHelloxml(String name) {
        return "<root>Hello " + name + ", Congrat! You created Spring Boot CXF XML API!!!</root>";
    }
    
}