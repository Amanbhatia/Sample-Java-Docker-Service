package com.mycompany;
import java.util.Arrays;

import org.apache.cxf.Bus;
import org.apache.cxf.endpoint.Server;
import org.apache.cxf.jaxrs.JAXRSServerFactoryBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.mycompany.rest.service.impl.HelloCXFImpl;

@SpringBootApplication
public class Start {

    @Autowired
    private Bus bus;

    public static void main(String[] args) {
        SpringApplication.run(Start.class, args);
    }
 
    @Bean
    public Server rsServer() {
        JAXRSServerFactoryBean endpoint = new JAXRSServerFactoryBean();
        endpoint.setBus(bus);
        endpoint.setServiceBeans(Arrays.<Object>asList(new HelloCXFImpl()));
        endpoint.setAddress("/");
        return endpoint.create();
    }
}