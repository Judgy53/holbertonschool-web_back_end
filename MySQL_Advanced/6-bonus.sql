-- Creates a stored procedure AddBonus that adds a new correction for a student.

-- Drop existing procedure
DROP PROCEDURE IF EXISTS AddBonus;

-- Redefine delimiter to be able to use `;` within the trigger
DELIMITER $$

-- Create procedure
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    DECLARE project_id INT;

    -- Select project id
    SELECT id INTO project_id 
        FROM projects 
        WHERE name = project_name;
    
    -- If project does not exist, create it and grab its generated id
    IF project_id IS NULL THEN
        INSERT INTO projects (name) 
            VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score) 
        VALUES (user_id, project_id, score);
END $$

-- Reset delimiter
DELIMITER ;