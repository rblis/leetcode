## Environment:
- Java version: 1.8
- Maven version: 3.*
- Spring Boot version: 2.2.1.RELEASE

## Read-Only Files:
- src/test/*

## Data:
Sample example of JSON data object:
```json
{
   "id": 1,
   "date": "1985-01-01",
   "firstName": "Foo",
   "lastName": "Bar",
   "phoneNumber": 3876542098
}
```

## Requirements:
The `REST` service must expose the `/endpoint` endpoint, which allows for managing the data records in the following way:


`POST` request to `/insert` :
* creates a new weather data record
* the response code is 201 and the response body is the created record, including its unique id


`GET` request to `/select`:
* the response code is 200
* the response body is an array of matching records, ordered by their ids in increasing order


`GET` request to `/select/<id>`:
* returns a record with the given id and status code 200
* if there is no record in the database with the given id, the response code is 404


`DELETE` request to `/delete/<id>`:
* deletes the record with the given id from the database and return status code 200
* if there was no record in the database with the given id, the response code is 404


Your task is to complete the given project so that it passes all the test cases when running the provided unit tests. The project by default supports the use of the H2 database, the datafiles will be loaded in folder structure as per the problem statement.

## Commands
- run: 
```bash
mvn clean package; java -jar target/project_jar-1.0.jar
```
- install: 
```bash
mvn clean install
```
- test: 
```bash
mvn clean test
```
/*
 * 
package com.hackerrank.sample;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
@DirtiesContext(classMode = DirtiesContext.ClassMode.BEFORE_EACH_TEST_METHOD)
@AutoConfigureMockMvc
public class SampleApplicationTests {
    @Autowired
    private MockMvc mockMvc;

    @Before
    public void setup() {
    }

    @Test
    public void defaultHelloTest() throws Exception {
        mockMvc.perform(get("/defaultHello"))
                .andDo(print())
                .andExpect(jsonPath("$.echo").value("Default Hello World!"))
                .andExpect(
                        status().isOk());
    }

    @Test
    public void defaultHelloWithParamTest() throws Exception {
        mockMvc.perform(get("/defaultHello")
                .param("message","False Message"))
                .andDo(print())
                .andExpect(jsonPath("$.echo").value("Default Hello World!"))
                .andExpect(
                        status().isOk());
    }

    @Test
    public void customHelloTest() throws Exception {
        mockMvc.perform(post("/customHello")
                .param("message", "Custom Hello World!"))
                .andDo(print())
                .andExpect(jsonPath("$.echo").value("Custom Custom Hello World!"))
                .andExpect(
                        status().isOk());
    }

    @Test
    public void customHelloWithEmptyParamTest() throws Exception {
        mockMvc.perform(post("/customHello")
                .param("message", ""))
                .andDo(print())
                .andExpect(jsonPath("$.echo").value("Custom "))
                .andExpect(
                        status().isOk());
    }

    @Test
    public void customHelloWithoutParamTest() throws Exception {
        mockMvc.perform(post("/customHello"))
                .andDo(print())
                .andExpect(
                        status().isBadRequest());
    }
}

 * 
 */