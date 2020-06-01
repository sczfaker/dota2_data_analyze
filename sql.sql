SELECT
matches.match_id,
matches.start_time,
((player_matches.player_slot < 128) = matches.radiant_win) win,
player_matches.hero_id,
player_matches.account_id,
leagues.name leaguename
FROM matches
JOIN match_patch using(match_id)
JOIN leagues using(leagueid)
JOIN player_matches using(match_id)
JOIN heroes on heroes.id = player_matches.hero_id
LEFT JOIN notable_players ON notable_players.account_id = player_matches.account_id
LEFT JOIN teams using(team_id)
WHERE TRUE
AND matches.start_time >= extract(epoch from timestamp '2020-06-30T17:51:53.887Z')
ORDER BY matches.match_id NULLS LAST
LIMIT 500