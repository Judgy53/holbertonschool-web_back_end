-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. 

-- Drop existing procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Redefine delimiter to be able to use `;` within the trigger
DELIMITER $$

-- Create procedure
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate average score
    SELECT AVG(corrections.score) INTO avg_score
        FROM corrections 
        WHERE corrections.user_id = user_id;

    -- Insert the score
    UPDATE users 
        SET users.average_score = avg_score 
        WHERE users.id = user_id;
END $$

-- Reset delimiter
DELIMITER ;