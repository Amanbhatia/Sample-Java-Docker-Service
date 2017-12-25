package com.mycompany.rest.service;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.springframework.stereotype.Service;
 
@Path("/helloCXF")
@Service
public interface HelloCXF {
 
    @GET
    @Path("/json/{name}")
    @Produces("application/json")
    String sayHelloJson(@PathParam("name") String a);

    @GET
    @Path("/xml/{name}")
    @Produces("application/xml")
    String sayHelloxml(@PathParam("name") String a);
    
}