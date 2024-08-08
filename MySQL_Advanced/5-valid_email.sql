-- Script that creates a trigger that resets `valid_email` only when the email has been changed.

-- Drop existing trigger
DROP TRIGGER IF EXISTS reset_valid_email;

-- Redefine delimiter to be able to use `;` within the trigger
DELIMITER $$

-- Create trigger
CREATE TRIGGER reset_valid_email
    BEFORE UPDATE ON users 
    FOR EACH ROW
    BEGIN
        IF NEW.email <> OLD.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END;
$$

-- Reset delimiter
DELIMITER ;
