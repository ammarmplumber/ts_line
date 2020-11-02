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
    name_in_url = 'block1'
    players_per_group = 4
    num_rounds = 10

    instructions_template = 'block1/instructions.html'
    instructions_new_template = 'block1/instructions_new.html'

    # payoffs if player picks green""",
    onegreen_payoff = c(0)
    twogreen_payoff = c(0)
    threegreen_payoff = c(0)
    fourgreen_payoff = c(0)

    # payoffs if player picks purple
    onepurple_payoff = c(0)
    twopurple_payoff = c(0)
    threepurple_payoff = c(0)
    fourpurple_payoff = c(0)

    # payoffs if player picks yellow
    oneyellow_payoff = c(3)
    twoyellow_payoff = c(6)
    threeyellow_payoff = c(9)
    fouryellow_payoff = c(12)


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        decisions = [
            p.decision for p in self.get_players() if p.decision != None
        ]
        if decisions:
            return dict(
                decisionlist=decisions
            )
        else:
            return dict(
                decisionlist='(no data)',
            )


class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            p.set_payoff()


class Player(BasePlayer):
    decision = models.StringField(
        widget=widgets.RadioSelectHorizontal
    )

    def decision_choices(self):
        import random
        choices = [['Green', 'Green'], ['Purple', 'Purple'], ['Yellow', 'Yellow']]
        random.shuffle(choices)
        return choices

    def other_player1(self):
        return self.get_others_in_group()[0]
    def other_player2(self):
        return self.get_others_in_group()[1]
    def other_player3(self):
        return self.get_others_in_group()[2]

    def set_payoff(self):
        greenval = 0
        purpleval = 0
        yellowval = 3
        todf = {'Green': [greenval, 2*greenval, 3*greenval, 4*greenval],
                'Purple': [purpleval, 2*purpleval, 3*purpleval, 4*purpleval],
                'Yellow': [yellowval, 2*yellowval, 3*yellowval, 4*yellowval]}
        payoff_matrix = pd.DataFrame(todf)

        choicecolumn = payoff_matrix[self.decision]
        self.payoff = choicecolumn[[self.other_player1().decision,
                                    self.other_player2().decision,
                                    self.other_player3().decision].count(self.decision)]



doc = """
This is a coordination game with 4 players.
"""