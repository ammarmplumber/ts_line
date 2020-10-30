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

doc = """
This is a coordination game with 4 players.
"""


class Constants(BaseConstants):
    name_in_url = 'line_set6'
    players_per_group = 4
    num_rounds = 5

    instructions_new_template = 'line_set6/instructions_new'
    instructions_template = 'line_set6/instructions.html'

    # payoffs if player picks red""",
    onered_payoff = c(7)
    twored_payoff = c(14)
    threered_payoff = c(21)
    fourred_payoff = c(28)

    # payoffs if player picks blue
    oneblue_payoff = c(5)
    twoblue_payoff = c(10)
    threeblue_payoff = c(15)
    fourblue_payoff = c(20)

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
        choices=[['Red', 'Red'], ['Blue', 'Blue'], ['Yellow', 'Yellow']],
        doc="""This player's decision""",
        widget=widgets.RadioSelectHorizontal,
    )

    comprehension_wrong_attempts = models.PositiveIntegerField()  # number of wrong attempts on understanding quesions page

    def other_player1(self):
        return self.get_others_in_group()[0]
    def other_player2(self):
        return self.get_others_in_group()[1]
    def other_player3(self):
        return self.get_others_in_group()[2]

    def set_payoff(self):
        redval = 0
        blueval = 0
        yellowval = 3
        todf = {'Red': [redval, 2*redval, 3*redval, 4*redval],
                'Blue': [blueval, 2*blueval, 3*blueval, 4*blueval],
                'Yellow': [yellowval, 2*yellowval, 3*yellowval, 4*yellowval]}
        payoff_matrix = pd.DataFrame(todf)

        choicecolumn = payoff_matrix[self.decision]
        self.payoff = choicecolumn[[self.other_player1().decision,
                                    self.other_player2().decision,
                                    self.other_player3().decision].count(self.decision)]



doc = """
This is a coordination game with 4 players.
"""