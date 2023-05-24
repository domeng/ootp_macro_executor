import pandas
from datautil.common import path_to_save_base

def load_dumped_csv(savefilename, filename):
    return pandas.read_csv(path_to_save_base(savefilename) + r"/import_export/csv/" + filename + ".csv")

def load_players(savefilename):
    p = load_dumped_csv(savefilename, 'players')    
    bat = load_dumped_csv(savefilename, 'players_batting')
    pit = load_dumped_csv(savefilename, 'players_pitching')

    return p.merge(bat, on='player_id').merge(pit, on='player_id')

def load_player_rating_map(savefilename):
    players_df = load_players(savefilename)
    rating_map = players_df.set_index('player_id').T.to_dict()

    return rating_map