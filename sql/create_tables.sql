-- create the databases
CREATE DATABASE IF NOT EXISTS test_db;

-- create the table
CREATE TABLE IF NOT EXISTS test_info (
    id int NOT NULL PRIMARY KEY,
    create_time DATETIME,
    name varchar(255),
    type int
);
