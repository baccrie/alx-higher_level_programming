#!/usr/bin/sql
-- creates a new table with Null constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, state NOT NULL FOREIGN KEY(id) REFRENCES state(id), name VARCHAR(256)) type=InnoDB;
