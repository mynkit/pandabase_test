SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;
SET CHARACTER_SET_DATABASE = utf8;
SET CHARACTER_SET_SERVER = utf8;

DROP DATABASE IF EXISTS sample_db;
CREATE DATABASE sample_db DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE sample_db;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  name VARCHAR(256),
  age INT
);

INSERT INTO users (
  id,
  name,
  age
) VALUES (
  1,
  "taro",
  20
),
(
  2,
  "jiro",
  17
),
(
  3,
  "saburo",
  18
);
