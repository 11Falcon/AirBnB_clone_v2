-- create hbnb_test_db database 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a test user hbnb_test 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pw';

-- set all privileges on hbnb_test_db
GRANT ALL PRIVLEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- set permitions for performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
