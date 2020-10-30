from multiprocessing.reduction import register

from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class Autonomy_1(Page):
    form_model = 'player'
    form_fields = ['autgen_1_1', 'autgen_1_2', 'autgen_1_3', 'autgen_1_4', 'autgen_1_5', 'autgen_1_6', 'autgen_1_7', 'autgen_1_8']

class Autonomy_2(Page):
    form_model = 'player'
    form_fields = ['autgen_2_1', 'autgen_2_2', 'autgen_2_3', 'autgen_2_4', 'autgen_2_5', 'autgen_2_6', 'autgen_2_7', 'autgen_2_8', 'autgen_2_9']


page_sequence = [Demographics, Autonomy_1, Autonomy_2]
