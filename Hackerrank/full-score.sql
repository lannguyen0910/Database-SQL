SELECT h.hacker_id, h.name from hackers h, challenges c, difficulty d, submissions s
WHERE h.hacker_id = s.hacker_id AND c.difficulty_level = d.difficulty_level 
AND c.challenge_id = s.challenge_id AND s.score = d.score
GROUP BY h.hacker_id, h.name 
HAVING COUNT(h.hacker_id) > 1
ORDER BY COUNT(c.challenge_id) DESC, h.hacker_id