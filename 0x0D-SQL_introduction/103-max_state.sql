-- Displays the max temperature of each state(order by State name).
SELECT state , MAX(value) AS max_temp
FROM remperatures
GROUP BY state
ORDER BY state;
