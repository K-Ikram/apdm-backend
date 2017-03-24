set names 'utf8';
drop  database if exists  apdm;
create database apdm
character set utf8
collate utf8_bin;
use apdm;

create table client(
client_id int auto_increment,
gender enum('homme','femme'),
phone_contact varchar(50) not null,
phone_sms varchar(50) not null,
language varchar(50),
comments varchar(100),
primary key(client_id)
);

create table city(
city_id int auto_increment,
city_name varchar(50) not null,
primary key(city_id)
);

create table farm(
farm_id int auto_increment,
farm_name varchar(50) not null,
city_id varchar(50) not null,
comments varchar(100),
primary key(farm_id),
foreign key(city_id) references city(city_id)
);

create table plot(
plot_id int auto_increment,
plot_name varchar(50) not null,
latitude_n double not null default 0,
longitude_n double not null default 0,
latitude_s double not null default 0,
longitude_s double not null default 0,
soil_type enum('aride','semi-aride'),
farm_id int not null,
comments varchar(50),
primary key(plot_id),
foreign key(farm_id) references farm(farm_id)
);

create table crop_production(
crop_production_id int auto_increment,
crop enum('wheat', 'potato','tomato','rice'),
name varchar(50) not null,
start_date date not null,
end_date date,
yield double,
plot_id int not null,
comments varchar(100),
primary key(crop_production_id),
foreign key(plot_id) references plot(plot_id)
);

create table sensor(
sensor_id int auto_increment,
sensor_type varchar(20) not null,
sensor_unit varchar(20) not null,
primary key(sensor_id)
);

create table measure(
measure_id int auto_increment,
measure_value double not null,
measure_timestamp timestamp not null,
sensor_id int not null,
primary key(measure_id),
foreign key(sensor_id) references sensor(sensor_id)
);

create table disease(
disease_id int auto_increment,
disease_name varchar(50) not null,
primary key(disease_id)
);

create table anomaly(
anomaly_id int auto_increment,
occurence_date datetime not null,
reporting_date datetime not null,
client_id int not null,
crop_production_id int not null,
disease_id int not null,
treated boolean default false,
primary key(anomaly_id),
foreign key(client_id) references client(client_id),
foreign key(crop_production_id) references crop_production(crop_production_id),
foreign key(disease_id) references disease(disease_id)
);

create table alert(
alert_id int auto_increment,
alert_date datetime not null,
crop_production_id int not null,
disease_id int not null,
risk_rate float not null,
feedback_date datetime,
feedback_type enum('confirmed','denied'),
client_id int,
primary key(alert_id),
foreign key(client_id) references client(client_id),
foreign key(crop_production_id) references crop_production(crop_production_id),
foreign key(disease_id) references disease(disease_id)
);

-- create table crop_production_disease(
-- crop_production_id int not null references crop_production(crop_production_id),
-- disease_id int not null references disease(disease_id),
-- primary key(crop_production_id,disease_id)

-- );

-- create table farm_client(
-- farm_id int not null references farm(farm_id),
-- client_id int not null references client(client_id),
-- primary key(farm_id, client_id)
-- );

-- create table sensor_plot(
-- sensor_id int not null references sensor(sensor_id),
-- plot_id int not null references plot(plot_id),
-- date_debut date not null,
-- date_fin date,
-- primary key(sensor_id, plot_id, date_debut)
-- );

-- create table crop_production_sensor(
-- crop_production_id int not null references crop_production(crop_production_id),
-- sensor_id int not null references sensor(sensor_id),
-- primary key(crop_production_id,sensor_id)
-- );


CREATE TABLE  fhb_training_set
(
  training_set_id int NOT NULL AUTO_INCREMENT,
  temp_duration float  NOT NULL , # durée de temperature entre 9 et 30 °C durant une semaine avant le jour de prévision
  humidity_avg float NOT NULL,  # moyenne de l'humidité relative durant une semaine avant le jour de prévision
  rainfall_duration float NOT NULL, # durée des précipitations durant une semaine avant le jour de prévision
  weight float DEFAULT 1,
  class varchar(10) NOT NULL,
  primary key(training_set_id)
);
CREATE TABLE  fhb_predictions
(
  prediction_id int NOT NULL AUTO_INCREMENT,

  prediction_date timestamp not null,
  crop_production_id int not null,
  temp_duration float  NOT NULL , # durée de temperature entre 9 et 30 °C durant une semaine avant le jour de prévision
  humidity_avg float NOT NULL,  # moyenne de l'humidité relative durant une semaine avant le jour de prévision
  rainfall_duration float NOT NULL, # durée des précipitations durant une semaine avant le jour de prévision
  class VARCHAR(10) NOT NULL,
  risk_rate float NOT NULL,

  primary key(prediction_id),
  foreign key(crop_production_id) references crop_production(crop_production_id)

);

CREATE TABLE fhb_neighborhood
(
  prediction_id int NOT NULL references fhb_predictions(prediction_id),
  training_set_id int not null references fhb_training_set(training_set_id),
  primary key(prediction_id, training_set_id)
);

INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'humidity', '%');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'humidity', '%');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'humidity', '%');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'humidity', '%');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'temperature', '°C');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'temperature', '°C');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'temperature', '°C');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'temperature', '°C');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'temperature', '°C');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'rainfall', 'mm');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'rainfall', 'mm');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'rainfall', 'mm');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'rainfall', 'mm');
INSERT INTO `sensor` (`sensor_id`, `sensor_type`, `sensor_unit`) VALUES (NULL, 'rainfall', 'mm');

INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'farma', '19', NULL);
INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'farmb', '9', NULL);
INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'farmc', '1', NULL);
INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'new farm', '2', NULL);
INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'farmyy', '22', NULL);
INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'farm', '48', NULL);
INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'farm abc', '26', NULL);
INSERT INTO `farm` (`farm_id`, `farm_name`, `city_id`, `comments`) VALUES (NULL, 'smartfarm', '16', NULL);

--INSERT INTO `client` (`client_id`, `name`, `surname`, `gender`, `email`, `phone_contact`, `phone_sms`, `language`, `comments`) VALUES (NULL, 'rafed', 'wassila', 'femme', 'cw_rafed@esi.dz', '+213797820473', '+213797820473', 'english', NULL);
--INSERT INTO `client` (`client_id`, `name`, `surname`, `gender`, `email`, `phone_contact`, `phone_sms`, `language`, `comments`) VALUES (NULL, 'karouche', 'ikram', 'femme', 'ci_karouche@esi.dz', '+213797820473', '+213797820473', 'english', NULL);
--INSERT INTO `client` (`client_id`, `name`, `surname`, `gender`, `email`, `phone_contact`, `phone_sms`, `language`, `comments`) VALUES (NULL, 'ilmane', 'nassim', 'homme', 'nassim.ilmane@gmail.com', '+213797820473', '+213797820473', 'english', NULL);

INSERT INTO `plot` (`plot_id`, `plot_name`, `soil_type`, `farm_id`, `comments`) VALUES (NULL, 'plot in metidja', 'aride', '2', NULL);
INSERT INTO `plot` (`plot_id`, `plot_name`, `soil_type`, `farm_id`, `comments`) VALUES (NULL, 'plot in farm_ida', 'aride', '3', NULL);
INSERT INTO `plot` (`plot_id`, `plot_name`, `soil_type`, `farm_id`, `comments`) VALUES (NULL, 'plot in farm_ida', 'aride', '3', NULL);
INSERT INTO `plot` (`plot_id`, `plot_name`, `soil_type`, `farm_id`, `comments`) VALUES (NULL, 'plot in metidja', 'aride', '2', NULL);
INSERT INTO `plot` (`plot_id`, `plot_name`, `soil_type`, `farm_id`, `comments`) VALUES (NULL, 'plot in metidja', 'aride', '2', NULL);

INSERT INTO `crop_production` (`crop_production_id`, `name`, `start_date`, `end_date`, `yield`, `plot_id`, `crop`, `comments`) VALUES (NULL, 'crop production of wheat', '2017-02-01', '2017-04-20', NULL, '1', '1', NULL);
INSERT INTO `crop_production` (`crop_production_id`, `name`, `start_date`, `end_date`, `yield`, `plot_id`, `crop`, `comments`) VALUES (NULL, 'crop production of wheat', '2017-02-01', '2017-04-20', NULL, '1', '1', NULL);
INSERT INTO `crop_production` (`crop_production_id`, `name`, `start_date`, `end_date`, `yield`, `plot_id`, `crop`, `comments`) VALUES (NULL, 'crop production of wheat', '2017-02-01', '2017-04-20', NULL, '1', '1', NULL);
INSERT INTO `crop_production` (`crop_production_id`, `name`, `start_date`, `end_date`, `yield`, `plot_id`, `crop`, `comments`) VALUES (NULL, 'crop production of wheat', '2017-02-01', '2017-04-20', NULL, '1', '1', NULL);
INSERT INTO `crop_production` (`crop_production_id`, `name`, `start_date`, `end_date`, `yield`, `plot_id`, `crop`, `comments`) VALUES (NULL, 'crop production of wheat', '2017-02-01', '2017-04-20', NULL, '1', '1', NULL);
INSERT INTO `crop_production` (`crop_production_id`, `name`, `start_date`, `end_date`, `yield`, `plot_id`, `crop`, `comments`) VALUES (NULL, 'crop production', '2017-02-01', '2017-05-20', NULL, '1', '1', NULL);
INSERT INTO `crop_production` (`crop_production_id`, `name`, `start_date`, `end_date`, `yield`, `plot_id`, `crop`, `comments`) VALUES (NULL, 'crop production', '2017-02-01', '2017-05-20', NULL, '1', '1', NULL);

INSERT INTO `disease` (`disease_id`, `disease_name`) VALUES (NULL, 'mildiou');
INSERT INTO `disease` (`disease_id`, `disease_name`) VALUES (NULL, 'pourriture racinaire');
INSERT INTO `disease` (`disease_id`, `disease_name`) VALUES (NULL, 'pyriculariose');

INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '15', NOW(), '5');

INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '95', NOW(), '1');

INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');
INSERT INTO `measure` (`measure_id`, `measure_value`, `measure_timestamp`, `sensor_id`) VALUES (NULL, '0.8', NOW(), '10');

/*Cities*/
Insert into city (city_id, city_name) values (1,'Adrar');
Insert into city (city_id, city_name) values (2,'Chlef');
Insert into city (city_id, city_name) values (3,'Laghouat');
Insert into city (city_id, city_name) values (4,'Oum El Bouaghi');
Insert into city (city_id, city_name) values (5,'Batna');
Insert into city (city_id, city_name) values (6,'Bejaia');
Insert into city (city_id, city_name) values (7,'Biskra');
Insert into city (city_id, city_name) values (8,'Bechar');
Insert into city (city_id, city_name) values (9,'Bl_ida');
Insert into city (city_id, city_name) values (10,'Bouira');
Insert into city (city_id, city_name) values (11,'Tamanrasset');
Insert into city (city_id, city_name) values (12,'Tebessa');
Insert into city (city_id, city_name) values (13,'Tlemcen');
Insert into city (city_id, city_name) values (14,'Tiaret');
Insert into city (city_id, city_name) values (15,'Tizi Ouzou');
Insert into city (city_id, city_name) values (16,'Alger');
Insert into city (city_id, city_name) values (17,'Djelfa');
Insert into city (city_id, city_name) values (18,'Jijel');
Insert into city (city_id, city_name) values (19,'Setif');
Insert into city (city_id, city_name) values (20,'Sa_ida');
Insert into city (city_id, city_name) values (21,'Skikda');
Insert into city (city_id, city_name) values (22,'S_idi Bel Abbes');
Insert into city (city_id, city_name) values (23,'Annaba');
Insert into city (city_id, city_name) values (24,'Guelma');
Insert into city (city_id, city_name) values (25,'Constantine');
Insert into city (city_id, city_name) values (26,'Medea');
Insert into city (city_id, city_name) values (27,'Mostaganem');
Insert into city (city_id, city_name) values (28,'M''Sila');
Insert into city (city_id, city_name) values (29,'Mascara');
Insert into city (city_id, city_name) values (30,'Ouargla');
Insert into city (city_id, city_name) values (31,'Oran');
Insert into city (city_id, city_name) values (32,'El Bayadh');
Insert into city (city_id, city_name) values (33,'Illizi');
Insert into city (city_id, city_name) values (34,'Bordj Bou Arrer_idj');
Insert into city (city_id, city_name) values (35,'Boumerdès');
Insert into city (city_id, city_name) values (36,'Tarf');
Insert into city (city_id, city_name) values (37,'Tindouf');
Insert into city (city_id, city_name) values (38,'Tissemsilt');
Insert into city (city_id, city_name) values (39,'El Oued');
Insert into city (city_id, city_name) values (40,'Khenchela');
Insert into city (city_id, city_name) values (41,'Souk Ahras');
Insert into city (city_id, city_name) values (42,'Tipaza');
Insert into city (city_id, city_name) values (43,'Mila');
Insert into city (city_id, city_name) values (44,'Ain Defla');
Insert into city (city_id, city_name) values (45,'Naama');
Insert into city (city_id, city_name) values (46,'Ain Timouchent');
Insert into city (city_id, city_name) values (47,'Ghardaia');
Insert into city (city_id, city_name) values (48,'Relizane');