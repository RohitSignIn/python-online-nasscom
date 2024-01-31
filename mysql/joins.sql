create database test;

use test;

create table customer (
	id int primary key,
    username text
);

create table transactions (
	id int primary key,
	amount int,
    cust_id int,
    foreign key(cust_id) references customer(id)
);

INSERT INTO transactions (id, amount, cust_id) 
VALUES (1, 500, 1),
(2, 500, 2),
(3, 500, 2),
(4, 500, 3);

SET SQL_SAFE_UPDATES = 0;

SELECT customer.username, 
transactions.amount
from customer
join transactions ON
customer.id = transactions.cust_id;


create table carts (
	id int primary key,
    username text
);

create table products (
	id int primary key,
    name text
);

create table cartproducts(
	cart_id int,
    prod_id int, 
    primary key(cart_id, prod_id),
    foreign key(cart_id) references carts(id),
    foreign key(prod_id) references products(id)
);

insert into cartproducts (cart_id, prod_id) 
values (1, 1),
(1, 2),
(3, 2),
(4, 3);

select 
carts.username,
products.name as prduct_name
from carts
left join cartproducts on 
cartproducts.cart_id = carts.id
left join products on 
cartproducts.prod_id = products.id

union

select 
carts.username,
products.name as prduct_name
from carts
right join cartproducts on 
cartproducts.cart_id = carts.id
right join products on 
cartproducts.prod_id = products.id;
