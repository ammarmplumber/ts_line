from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

from otreeutils.pages import AllGroupsWaitPage, ExtendedPage, UnderstandingQuestionsPage, APPS_DEBUG

class Introduction(Page):
    pass


class Contribute(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    body_text = "Waiting for other participants to decide."


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent1 = me.other_player1()
        opponent2 = me.other_player2()
        opponent3 = me.other_player3()
        return dict(
            my_decision=me.decision
        )


page_sequence = [Contribute, ResultsWaitPage, Results]