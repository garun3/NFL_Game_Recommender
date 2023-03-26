# NFL_Game_Recommender

This repository contains code for and NFL Game Recommender. It uses characteristics of a user-inputted game to recommend similar games using clustering methods. The application is built using Django.

#How To Run Shell Script

1. Run the command "chmod +x run_recommendation.sh"

2. Run the command "./run_recommendation.sh <GAME_ID> <NUM OF RECOMMENDED GAMES> <FULL RESULTS (0 or 1)>"

	For examples "./run_recommendation.sh 199212060buf 8 1"

To run web app:

1. Navigate to NFL_Game_Recommender/Backend/Backend
2. run command python manage.py runserver
