import pandas as pd 
import numpy as np
import sys

def find_closest_game(full_data, kmeans_result, input_game, num_games=5, full=1):
  cluster = kmeans_result[kmeans_result.game_id == input_game].labels.tolist()[0]
  diff = kmeans_result[kmeans_result.labels == cluster].iloc[:, 1:49].values - kmeans_result[kmeans_result.game_id == input_game].iloc[:, 1:49].values
  dists = []
  for d in diff:
    dists.append(np.linalg.norm(d))
  same_cluster = kmeans_result[kmeans_result.labels == cluster]
  same_cluster.loc[:,'distances'] = dists
  same_cluster = same_cluster.sort_values(by='distances')
  closest = same_cluster.game_id.tolist()[1:(num_games+1)]
  similar_games = full_data[full_data.game_id.isin(closest)]
  links = list('https://www.pro-football-reference.com/boxscores/' + similar_games['game_id'] + '.htm')

  if full:
    return similar_games, links
  else:
    #small_games = [similar_games['game_id'].values, similar_games["Week-Year"].values, similar_games['winning_name'].values, similar_games['losing_name'].values, 
    #               similar_games['winning_abbr'].values, similar_games['losing_abbr'].values]
    small_games = [similar_games["Week-Year"].values, similar_games['winning_name'].values, similar_games['losing_name'].values, similar_games['home_points'].values, similar_games['away_points'].values]
    small_games_reformat = []
    for i in range(len(small_games[0])):
      small_games_reformat.append([small_games[x][i] for x in range(len(small_games))])
    return small_games_reformat, links

if __name__ == "__main__":
  full_data_path = sys.argv[1]
  kmeans_path = sys.argv[2]
  input_game = sys.argv[3]
  num_games = int(sys.argv[4])
  full = int(sys.argv[5])
  

  full_data = pd.read_csv(full_data_path, index_col = False)
  kmeans_data = pd.read_csv(kmeans_path, index_col = False)
  
  print(find_closest_game(full_data, kmeans_data, input_game, num_games=num_games, full=full))