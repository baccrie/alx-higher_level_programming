#!/usr/bin/sql
-- creates a new table with Null constraints
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
