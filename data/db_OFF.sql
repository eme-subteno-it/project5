SET NAMES UTF8MB4;

-- ------------------------------------------------
-- Database db_OFF
-- ------------------------------------------------

CREATE DATABASE IF NOT EXISTS db_OFF;
USE db_OFF;

-- ------------------------------------------------
-- Table db_OFF.Category
-- ------------------------------------------------

CREATE TABLE IF NOT EXISTS Category (
    id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=InnoDB;

-- ------------------------------------------------
-- Table db_OFF.Users
-- ------------------------------------------------
CREATE TABLE IF NOT EXISTS Users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(16) NOT NULL,
    email VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=InnoDB;

-- ------------------------------------------------
-- Table db_OFF.Product
-- ------------------------------------------------
CREATE TABLE IF NOT EXISTS Product (
    id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=InnoDB;

-- ------------------------------------------------
-- Table db_OFF.Substitute
-- ------------------------------------------------
CREATE TABLE IF NOT EXISTS Substitute (
    id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL,
    subsitute_name VARCHAR(45) NOT NULL,
    substitute_desc VARCHAR(255) NULL,
    market_product VARCHAR(45) NULL,
    api_link VARCHAR(400) NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_product_subsitute
        FOREIGN KEY (product_id)
        REFERENCES Product(id)
)
ENGINE=InnoDB;

-- ------------------------------------------------
-- Table db_OFF.Category_product
-- ------------------------------------------------
CREATE TABLE IF NOT EXISTS Category_product (
    id_category INT NOT NULL,
    id_product INT NOT NULL,
    CONSTRAINT fk_category_id
        FOREIGN KEY (id_category)
        REFERENCES Category(id),
    CONSTRAINT fk_product_id
        FOREIGN KEY (id_product)
        REFERENCES Product(id)
)
ENGINE=InnoDB;

-- ------------------------------------------------
-- Table db_OFF Index
-- ------------------------------------------------
ALTER TABLE Category
ADD INDEX ind_category_name (category_name);

ALTER TABLE Product
ADD INDEX ind_product_name (product_name);