import pandas as pd 
import numpy as np
import sys
import os

from .game_rec.get_game_recs import find_closest_game

def get_game_recs(self, game_id, num_games, full):
        full_data_path = os.path.dirname(os.path.abspath(__file__)) + '/game_rec/all_data.csv'
        kmeans_path = os.path.dirname(os.path.abspath(__file__)) + '/game_rec/kmeans_data.csv'
        input_game = game_id
        num_games = int(num_games)
        full = int(full)

        full_data = pd.read_csv(full_data_path, index_col = False)
        kmeans_data = pd.read_csv(kmeans_path, index_col = False)
        
        return find_closest_game(full_data, kmeans_data, input_game, num_games=num_games, full=full)
    
def get_game_id(self, game, week, season):
    data_path = os.path.dirname(os.path.abspath(__file__)) + '/game_rec/basic_game_info.csv'

    ind_vs = game.index('vs')
    
    team1 = game[0:ind_vs-1]
    team2 = game[ind_vs+3:]
    week_year = week + '-' + season

    df = pd.read_csv(data_path, index_col = False)

    query = game + ' ' + season + ' Week ' + week

    try:
        df = df[df['Week-Year'] == week_year]
        df1 = df[df['home_team'].str.lower() == team1.lower()]
        df1 = df1[df1['away_team'].str.lower() == team2.lower()]
        df2 = df[df['home_team'].str.lower() == team2.lower()]
        df2 = df2[df2['away_team'].str.lower() == team1.lower()]

        if not df1.empty:
            game_id = df1['game_id'].values[0]
            return game_id, query
        elif not df2.empty:
            game_id = df2['game_id'].values[0]
            return game_id, query
    except:
        return None

def get_youtube_links(self, df):
    links = []
    for game in df:
        week_year = game[0]
        home_team = game[1]
        away_team = game[2]
        week, year = week_year.split('-')
        links.append(f'https://www.youtube.com/results?search_query={home_team}+vs+{away_team}+Week+{week}+{year}')
    return links