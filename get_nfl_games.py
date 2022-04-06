colcofrom sportsipy.nfl.boxscore import Boxscores, Boxscore
import pandas as pd 

seasons = [2000, 2010]
# for i in range(2015, 2020):
# 	games = Boxscores(1, i, 17)
# 	seasons.append(games.games)
# Pulls all games from weeks 7 and 8 in 2017
all_season_boxscores = pd.DataFrame()




for year in range(seasons[0], seasons[1]):
  print(year)
  games = Boxscores(1, year, 17)
  season_boxscores = list()
  for week in games.games.keys():
    print("    "+str(week))
    for game in games.games[week]:
      bx = Boxscore(game['boxscore'])
      bx_df = bx.dataframe
      bx_df.insert(0, "Week-Year", week, True)
      season_boxscores.append(bx_df)
  season_boxscores.insert(0, all_season_boxscores)
  all_season_boxscores = pd.concat(season_boxscores)
  all_season_boxscores.to_csv("nfl_"+str(seasons[0])+"_"+str(year)+"_boxscores.csv")

#print(all_season_boxscores.info())
all_season_boxscores.to_csv("nfl_"+str(seasons[0])+"_"+str(seasons[1]-1)+"_boxscores.csv")
