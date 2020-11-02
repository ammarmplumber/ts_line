from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

from otreeutils.pages import AllGroupsWaitPage, ExtendedPage, UnderstandingQuestionsPage, APPS_DEBUG

class Introduction(Page):
    pass

class SomeUnderstandingQuestions(UnderstandingQuestions_no_table):
    page_title = 'Comprehension Question - Set 2'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    questions = [
        {
            'question': 'For this set, what is the maximum payoff per round?',
            'options': [20, 12, 8, 28],
            'correct': 12,
            'hint': 'Please review instructions below.'
        },
    ]


page_sequence = [Introduction, SomeUnderstandingQuestions]