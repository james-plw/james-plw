DROP TABLE prem_data; #to reset

CREATE TABLE prem_data (
    id INT PRIMARY KEY, #identifier
    match_date DATE, 
    match_time TIME,
    matchweek TINYTEXT,
    match_day TINYTEXT,
    venue TINYTEXT,     #home or away
    result TINYTEXT,    #W / D / L
    gf INT,
    ga INT,
    opponent TINYTEXT,
    xg FLOAT,
    xga FLOAT,
    poss FLOAT,
    attendance FLOAT,
    formation TINYTEXT,
    referee TINYTEXT,
    sh FLOAT,           #number of shots
    sh_ot FLOAT,        #number of shots on targer
    avg_dist FLOAT,     #avg shot distance (metres?)
    fk FLOAT,           #number of free kicks taken
    pk INT,             #pens scored
    pk_att INT,         #pens attmpted
    team TINYTEXT
);

LOAD DATA INFILE 'prem_data.csv' 
INTO TABLE prem_data
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

SELECT * FROM prem_data;

#specific queries
SELECT team, xg, gf, venue, ga, xga, opponent
FROM prem_data
WHERE formation = '3-5-1-1';

#1 possession - xg correlation
SELECT poss, xg, team, venue, opponent
FROM prem_data
ORDER BY xg DESC;

#2 avg xg difference for each formation
SELECT ROUND(AVG(xg-xga), 3) as avg_xg_difference, formation, COUNT(formation)
FROM prem_data
GROUP BY formation
ORDER BY avg_xg_difference DESC;

#3 correlation xg/shot and average shot distance
SELECT xg, sh, sh_ot, ROUND(xg/sh, 2) AS avg_xg, avg_dist, team, gf, venue, ga, opponent
FROM prem_data
ORDER BY avg_xg DESC;

#4 xg table - xg difference for each team
SELECT team, ROUND(SUM(xg), 1) as xg_for, 
        ROUND(SUM(xga), 1) as xg_against, 
        ROUND(SUM(xg-xga), 1) AS xg_difference 
FROM prem_data
GROUP BY team
ORDER BY xg_difference DESC;

#5 which team created highest quality chances? xg/shot
SELECT team, ROUND(AVG(xg/sh), 2) AS avg_xg,
        ROUND(SUM(xg), 1) AS total_xg_for,
        SUM(sh) AS total_shot
FROM prem_data
GROUP BY team
ORDER BY avg_xg DESC;

#6 goals per shot(conversion rate) against avg shot distance
SELECT sh, ROUND(gf/sh, 2) AS conv_rate, avg_dist, team, gf, venue, ga, opponent
FROM prem_data
ORDER BY conv_rate DESC;

#7 total goals and xg for each timeslot
#which days had the most goals per game
SELECT ROUND(AVG(gf + ga), 2) AS avg_goals, ROUND(AVG(xg), 2) AS avg_xg, match_day, COUNT (match_day)
FROM prem_data
GROUP BY match_day
ORDER BY avg_goals DESC;
#which time slots had the most goals per game
SELECT ROUND(AVG(gf + ga), 2) AS avg_goals, ROUND(AVG(xg + xga), 2) AS avg_xg, match_day, match_time, 
        ROUND(COUNT(match_day AND match_time) / 2, 0) AS timeslot_count
FROM prem_data
GROUP BY match_day, match_time
HAVING COUNT(match_day AND match_time) / 2 > 5
ORDER BY avg_goals DESC;

#8 referee vs home/away points
SELECT referee,
    ROUND(COUNT(referee)/2, 0) AS ref_count,
    ROUND(SUM(CASE
            WHEN venue = 'Home' AND result = 'W' THEN 3
            WHEN venue = 'Home' AND result = 'D' THEN 1
            ELSE 0
    END) / (COUNT(referee)/2) , 2) AS avg_home_points,

    ROUND(SUM(CASE
            WHEN venue = 'Away' AND result = 'W' THEN 3
            WHEN venue = 'Away' AND result = 'D' THEN 1
            ELSE 0
    END) / (COUNT(referee)/2) , 2) AS avg_away_points
FROM prem_data
GROUP BY referee
ORDER BY ref_count DESC;