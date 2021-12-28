package com.shepherd.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**@author shepherd
 * @SpringBootApplication：标注这个类是一个springboot应用
 * **/
@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        //将springboot应用启动
        SpringApplication.run(DemoApplication.class, args);
    }

}
