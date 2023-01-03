# use 2007-2011 drafts to develop a solid prediction model for NBA Draft
# College stats taken into account: PPG, APG, RPG, SPG, BPG, FG%, Pos, MPG
# Success measure: Stats, Games Played, Years in NBA, Money Earned - combine to some metric?
# Step 1: Use Drafts 07-11 as training, 2012,13 as test
# - Make an object with all relevant info? How to Plot? Equation?
# Step 2: Plot 7-11, 12,13
# Step 3: Calculate MSE to show similarity and efficiency of model
from enum import Enum

class Position(Enum):
    Guard = 1
    Forward = 2
    Center = 3

class Player:
    def __init__(self, pos, c_ppg, c_rpg, c_apg, c_fg_pct, c_bpg, c_spg, c_sos,
                 avg_ppg, avg_rpg, avg_apg, avg_fg_pct, avg_spg, avg_bpg,
                 all_star, all_nba):
        self.pos = pos
        self.c_ppg = c_ppg
        self.c_rpg = c_rpg
        self.c_apg = c_apg
        self.c_fg_pct = c_fg_pct
        self.c_bpg = c_bpg
        self.c_spg = c_spg
        self.c_sos = c_sos
        self.avg_ppg = avg_ppg
        self.avg_rpg = avg_rpg
        self.avg_apg = avg_apg
        self.avg_fg_pct = avg_fg_pct
        self.avg_bpg = avg_bpg
        self.avg_spg = avg_spg
        self.all_star = all_star
        self.all_nba = all_nba


def get_x_arr(player):
    return [[player.c_ppg], [player.c_rpg], [player.c_apg], [player.c_fg_pct],
            [player.c_bpg], [player.c_spg], [player.c_sos]]


def get_y_arr(stat):
    return [stat]



