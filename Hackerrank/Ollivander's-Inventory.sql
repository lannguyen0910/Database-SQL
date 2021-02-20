SELECT W.id, WP.age, W.coins_needed, W.power
FROM Wands_Property WP, Wands W
WHERE WP.is_evil = 0 AND W.code = WP.code
AND W.coins_needed = (SELECT MIN(W1.coins_needed) FROM Wands W1, Wands_Property WP1 
                      WHERE W1.code = WP1.code AND W.power = W1.power AND WP.age = WP1.age)
ORDER BY W.power DESC, WP.age DESC;