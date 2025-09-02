/* banco de dados tropa do Mael*/

create database ecomerce;

use ecomerce;

create table dados(
	nome varchar(1000),
	vendedor varchar(100),
	avaliacao float(2,1)
	reviews int,
	preco_antigo float(10,2),
	preco_atual float(10,2),
	source varchar(200),
	data_extracao varchar(200)
);