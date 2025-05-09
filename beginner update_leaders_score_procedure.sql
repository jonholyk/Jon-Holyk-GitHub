DELIMITER @
CREATE PROCEDURE UPDATE_LEADERS_SCORE (IN in_School_ID INT, IN in_Leader_Score INT)
    LANGUAGE SQL
    BEGIN
        IF in_Leader_Score >= 0 AND in_Leader_Score < 20 THEN
            UPDATE CHICAGO_PUBLIC_SCHOOLS
            SET Leaders_Icon = 'Very weak'
            WHERE School_ID = in_School_ID;
        ELSEIF in_Leader_Score < 40 THEN
            UPDATE CHICAGO_PUBLIC_SCHOOLS
            SET Leaders_Icon = 'Weak'
            WHERE School_ ID = in_School_ID;
        ELSEIF in_Leader_Score < 60 THEN
            UPDATE CHICAGO_PUBLIC_SCHOOLS
            SET Leaders_Icon = 'Average'
            WHERE School_ID = in_School_ID;
        ELSEIF in_Leader_Score < 80 THEN
            UPDATE CHICAGO_PUBLIC_SCHOOLS
            SET Leaders_Icon = 'Strong'
            WHERE School_ID = in_School_ID;
        ELSE
            UPDATE CHICAGO_PUBLIC_SCHOOLS
            SET Leaders_Icon = 'Very Strong'
            WHERE School_ID = in_School_ID;
        END IF;
    END@
DELIMITER;