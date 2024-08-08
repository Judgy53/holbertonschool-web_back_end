-- Creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

-- Drop existing procedure
DROP FUNCTION IF EXISTS SafeDiv;

-- Redefine delimiter to be able to use `;` within the trigger
DELIMITER $$

-- Create procedure
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;

    IF b = 0 THEN 
        SET result = 0;
    ELSE 
        SET result = a / b;
    END IF;

    RETURN result;
END $$

-- Reset delimiter
DELIMITER ;