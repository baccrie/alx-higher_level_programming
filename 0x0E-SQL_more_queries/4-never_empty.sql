#!/usr/bin/sql
-- creates a new table with Null constraints
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
