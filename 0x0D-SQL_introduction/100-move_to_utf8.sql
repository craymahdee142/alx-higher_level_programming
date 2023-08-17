-- Converts database hbtn_oc_0to UTF

USE `hbtn_0c_0` 
ALTER TABLE first_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
