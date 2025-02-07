SELECT event_time, temp FROM project_test
GROUP BY event_time, temp
ORDER BY temp DESC;