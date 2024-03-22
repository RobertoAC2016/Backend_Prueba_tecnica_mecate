CREATE DATABASE IF NOT EXISTS registro;

USE registro;

CREATE TABLE IF NOT EXISTS `aerolineas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `aeropuertos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `movimientos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`descripcion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `vuelos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_aerolinea` int NULL,
  `id_aeropuerto` int NULL,
  `id_movimiento` int NULL,
  `dia` datetime DEFAULT now(),
  PRIMARY KEY (`id`),
  UNIQUE KEY (`id_aerolinea`, `id_aeropuerto`, `id_movimiento`, `dia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT IGNORE INTO aerolineas (nombre) VALUES ('Volaris'), ('Aeromar'), ('Interjet'), ('Aeromexico');
INSERT IGNORE INTO aeropuertos (nombre) VALUES ('Benito Juarez'), ('Guanajuato'), ('La paz'), ('Oaxaca');
INSERT IGNORE INTO movimientos (descripcion) VALUES ('Salida'), ('Llegada');
INSERT IGNORE INTO vuelos (`id_aerolinea`, `id_aeropuerto`, `id_movimiento`, `dia`) VALUES 
('1', '1', '1', '2021-05-02'),
('2', '1', '1', '2021-05-02'),
('3', '2', '2', '2021-05-02'),
('4', '3', '2', '2021-05-02'),
('1', '3', '2', '2021-05-02'),
('2', '1', '1', '2021-05-02'),
('2', '3', '1', '2021-05-04'),
('3', '4', '1', '2021-05-04'),
('3', '4', '1', '2021-05-04');