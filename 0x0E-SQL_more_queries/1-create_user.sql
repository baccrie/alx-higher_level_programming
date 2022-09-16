#!/usr/bin/sql
-- creates a user and give all priviledges
CREATE USER user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd IF NOT EXISTS;
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
