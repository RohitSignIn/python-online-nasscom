
-- Create Database
create database studentDb;

-- Use a Database
use studentdb;

-- Creating table
create table class10(
	id int auto_increment primary key,
	name text,
    email text,
    phone long
);

-- Changing Structure of Table
ALTER TABLE class10 ADD id int;
ALTER TABLE class10 ADD primary key(id);


-- Insert into Table
insert into class10 (name, email, phone) 
values("Rohit", "rohit@gmail.com", 7894561232);


-- Fetch data from table
SELECT * FROM class10; 
SELECT name,email FROM class10;