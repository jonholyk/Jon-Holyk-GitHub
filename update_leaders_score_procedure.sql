DELIMITER @
CREATE PROCEDURE UPDATE_LEADERS_SCORE (IN in_School_ID INT, IN in_Leader_Score INT)
	LANGUAGE SQL
BEGIN
    START TRANSACTION;

    IF in_Leader_Score >= 0 AND in_Leader_Score < 20 THEN
        UPDATE chicago_public_schools
        SET Leaders_Icon = 'Very weak'
        WHERE School_ID = in_School_ID;
        
    ELSEIF in_Leader_Score < 40 THEN
        UPDATE chicago_public_schools
        SET Leaders_Icon = 'Weak'
        WHERE School_ID = in_School_ID;
        
    ELSEIF in_Leader_Score < 60 THEN
        UPDATE chicago_public_schools
        SET Leaders_Icon = 'Average'
        WHERE School_ID = in_School_ID;
        
    ELSEIF in_Leader_Score < 80 THEN
        UPDATE chicago_public_schools
        SET Leaders_Icon = 'Strong'
        WHERE School_ID = in_School_ID;
        
    ELSEIF in_Leader_Score <= 99 THEN
        UPDATE chicago_public_schools
        SET Leaders_Icon = 'Very Strong'
        WHERE School_ID = in_School_ID;

    ELSE
        ROLLBACK;
    END IF;

    COMMIT;
END@
DELIMITER ;