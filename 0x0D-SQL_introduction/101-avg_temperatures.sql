-- Displays the average tempurature

SELECT city, AVG(value) AS TEMP FROM tempeartures as GROUP BY city ORDER BY avg temp DESC;
