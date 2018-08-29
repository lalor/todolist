-- we don't know how to generate schema flask_navi (class Schema) :(
create table if not exists grouplist
(
	id int auto_increment
		primary key,
	parent_id int null,
	name varchar(64) null
)
;

create table if not exists sitelist
(
	id int auto_increment
		primary key,
	user_id int not null,
	group_id int default '0' null,
	title varchar(1024) not null,
	url varchar(1024) null,
	description varchar(1024) null,
	status int(2) not null comment '是否显示',
	create_time int not null
)
charset=utf8
;

create table if not exists user
(
	id int auto_increment
		primary key,
	username varchar(24) null,
	password varchar(24) null
)
;


