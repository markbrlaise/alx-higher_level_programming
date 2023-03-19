-- Create database hbtn_0e_14_usa, tables states and cities + some data
create database if not exists hbtn_0e_14_usa;
use hbtn_0e_14_usa;

create table if not exists states (
	id int not null auto_increment,
	name varchar(256) not null,
	primary key (id)
);

insert into states (name) values ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

create table if not exists cities (
	id int not null auto_increment,
	state_id int not null,
	name varchar(256) not null,
	primary key (id),
	foreign key(state_id) references states(id)
);

INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
