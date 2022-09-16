#!/usr/bin/sql
-- creates a new user and new databases with limited privilege
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;
GRANT SELECT ON hbtn_0d_2 . * TO user_0d_2@localhost;
