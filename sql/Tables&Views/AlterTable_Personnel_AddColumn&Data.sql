ALTER TABLE Personnel
ADD COLUMN Department_ID CHAR(2);

UPDATE Personnel
SET Department_ID = CASE 
    WHEN ID % 4 = 0 THEN 'HR'
    WHEN ID % 4 = 1 THEN 'IT'
    WHEN ID % 4 = 2 THEN 'FN'
    ELSE 'OP'
END;