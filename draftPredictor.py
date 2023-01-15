import math
from enum import Enum


class Position(Enum):
    Guard = 1
    Forward = 2
    Center = 3


class Player:
    def __init__(self, pos, c_ppg, c_rpg, c_apg, c_fg_pct, c_spg, c_bpg,
                 tenyr_p, tenyr_r, tenyr_a, tenyr_s, tenyr_b,
                 all_star, all_nba):
        self.pos = pos
        self.c_ppg = c_ppg
        self.c_rpg = c_rpg
        self.c_apg = c_apg
        self.c_fg_pct = c_fg_pct
        self.c_spg = c_spg
        self.c_bpg = c_bpg
        self.tenyr_p = tenyr_p
        self.tenyr_r = tenyr_r
        self.tenyr_a = tenyr_a
        self.tenyr_s = tenyr_s
        self.tenyr_b = tenyr_b
        self.all_star = all_star
        self.all_nba = all_nba


def get_x_arr(player):
    return [[1], [math.sqrt(player.c_ppg + player.c_apg + player.c_rpg +
                         (10 * (player.c_fg_pct + player.c_spg + player.c_bpg)))]]


def get_y_arr(stat):
    return [stat]



