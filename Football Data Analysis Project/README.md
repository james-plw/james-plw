# :soccer: Football Data Analysis Project - Analysing and Visualising Data From the 2023-24 Premier League season

## Objective

In this project, I analysed data from the 2023-24 Premier League season to produce some fun visualisations:
* The dataset included basic stats and information about every PL game, including expected goals (xG).
* I planned to ask myself some questions about the data, and then attempt to answer them while demonstrating my ability with key analytical tools.
* The questions I asked ranged from finding the correlation between a team's possession, and the xG they create, to the most exciting timeslot according to average goals.
* The tools I used were Python (for manipulating & cleaning), SQL (for queries and analysis) and Tableau (for interactive visualisations).

The sections below will explain additional details on the data and technologies utilized.

## Table of Contents

- [Dataset Used](#dataset-used)
- [Technologies](#technologies)
- [Questions](#questions)
- [Methods](#methods)
- [Results](#results)
- [Still interested?](#still-interested)

## Dataset Used

* This project used data I downloaded from [Kaggle.](https://www.kaggle.com/datasets/mertbayraktar/english-premier-league-matches-20232024-season?resource=download)
* It was downloaded in a csv format, and had the following data for every Premier League match last season:
* Date, Day & Time, Round, Team, Venue(Home/Away), Opponent, Result(W/D/L), Goals For & Against, xG For & Against, Possession(for the 'Team'), Shots & Shots on Target, Average Shot Distance, Number of Free Kicks taken, Penalties taken & Penalties scored, Attendance, Captain, Formation, Referee.
* It also included some less useful columns such as: Competition, Match Report, Notes and Season that each had 1 unique value.
* There were 760 rows of data: 380 games in a season, with data from both teams per match

## Technologies

The following technologies are used to build this project:
- Language: Python for cleaning, MySQL for analysis
- Libraries: pandas, numpy
- IDE: Spyder 
- Visualisation: Tableau Public

## Questions
1. How do xG and Possession correlate?
2. What is the best formation?
3. How does the xG per shot correlate with the average shot distance in that game?
4. How would the league table look according the total xG difference?
5. Which team created the highest quality chances on average?
6. How does a team's conversion rate correlate with average shot distance in that game?
7. What is the most exciting timeslot for a match?
8. Did any referee have a particular bias towards home or away teams?

## Methods

* I imported the data into Python, using pandas to read the csv file and convert it into a numpy array.
* After assessing the data, I removed the less useful data mentioned above, along with 'Captain' (not relevant to any of the planned analysis)
* I also removed the index column, as the numbers were repeated for some reason, and re-added it when exporting the data to a new csv using pandas, for an index that actually ran from 0 to 759.
* I then imported this new csv file to a MySQL server and ran various queries to investigate the answers to my questions.
* For most of the questions, I exported the data returned by the queries to visualise in Tableau.

## Results

* A non-interactive image of the dashboard I created in Tableau is shown below. The interactive version can be found [here and is based viewed on desktop.](https://public.tableau.com/app/profile/james.wright3486/viz/PremierLeague2324DataAnalysis/PremierLeague2324DataAnalysis)

![Premier League 23_24 Data Analysis](https://github.com/user-attachments/assets/ecd1a157-728d-44e3-987c-0f027b03c528)

* 

## Still interested?

* To view the Python script I used to clean the data see the [script here.](prem_analysis.py)
* For all of my SQL queries, but in a less wordy format, view the [SQL file here.](prem_queries.sql)
* As previously linked, the interactive dashboard for this porject can be found [here.](https://public.tableau.com/app/profile/james.wright3486/viz/PremierLeague2324DataAnalysis/PremierLeague2324DataAnalysis)

***
