package com.shepherd.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author shepherd
 * @Controller
 * */
@RestController
@RequestMapping("/hello")
public class HelloController{
    @GetMapping("/hello.action")
    /**
     * @ResponseBody
     * 和Controller配合使用，否则会报404错误
     */
    public String hello(){
        return "Hello World";
    }
}
