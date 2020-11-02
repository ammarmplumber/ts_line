from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy as np
import pandas as pd
import random

doc = """
This is a coordination game with 4 players.
"""


class Constants(BaseConstants):
    name_in_url = 'understanding_b1'
    players_per_group = 4
    num_rounds = 1

    instructions_new_template = 'understanding_b1/instructions_new.html'
    instructions_template = 'understanding_b1/instructions.html'


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    comprehension_wrong_attempts = models.PositiveIntegerField()   # number of wrong attempts on understanding quesions page


doc = """
This is a coordination game with 4 players.
"""