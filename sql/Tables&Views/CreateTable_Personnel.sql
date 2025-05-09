CREATE TABLE Personnel (
    ID INT NOT NULL PRIMARY KEY,
    F_Name VARCHAR(15) NOT NULL,
    L_Name VARCHAR(15) NOT NULL,
    SSN CHAR(9) UNIQUE,
    DOB DATE,
    SALARY DECIMAL(8,2),
    CITY VARCHAR(15),
    STATE CHAR(2),
    HIRE_DATE Date
    );
    
INSERT INTO Personnel (ID, F_Name, L_Name, SSN, DOB, SALARY, CITY, STATE, HIRE_DATE)
VALUES
(1, 'Alice', 'Smith', '123456789', '1985-04-12', 65000.00, 'Denver', 'CO', '2015-06-01'),
(2, 'Bob', 'Johnson', '987654321', '1990-09-23', 72000.00, 'Chicago', 'IL', '2017-08-15'),
(3, 'Carol', 'Lee', '456789123', '1979-12-01', 85000.00, 'Austin', 'TX', '2010-03-20'),
(4, 'David', 'Kim', '321654987', '1988-02-18', 50000.00, 'Seattle', 'WA', '2018-11-05'),
(5, 'Emma', 'Davis', '654321789', '1993-07-30', 57000.00, 'Phoenix', 'AZ', '2020-01-22');

SELECT * FROM Personnel;