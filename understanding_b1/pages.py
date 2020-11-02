from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


from otreeutils.pages import AllGroupsWaitPage, ExtendedPage, UnderstandingQuestionsPage, APPS_DEBUG

class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Sorting you into a group."

class Introduction(Page):
    pass

class Q(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 1
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    player_number = 0
    players = ['Q', 'R', 'T', 'S', 'Unknown']
    colors = ['Purple','Green','Yellow','Unknown']
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample([20, 12, 6, 28, 'Unknown'], 5),
            'correct': 12,
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[player_number],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
    ]

class R(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 2
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    player_number = 1
    players = ['Q', 'R', 'T', 'S', 'Unknown']
    colors = ['Purple','Green','Yellow','Unknown']
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample([20, 12, 6, 28, 'Unknown'], 5),
            'correct': 12,
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[player_number],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Yellow',
            'hint': 'Please review instructions below.'
        },
    ]


class T(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 3
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    player_number = 2
    players = ['Q', 'R', 'T', 'S', 'Unknown']
    colors = ['Purple','Green','Yellow','Unknown']
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample([20, 12, 6, 28, 'Unknown'], 5),
            'correct': 12,
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[player_number],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Yellow',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please review instructions below.'
        },
    ]


class S(UnderstandingQuestionsPage):
    def is_displayed(self):
        return self.player.id_in_group == 4
    page_title = 'Comprehension Questions'
    set_correct_answers = False   # do not fill out the correct answers in advance (this is for fast skipping through pages)
    form_model = 'player'
    form_field_n_wrong_attempts = 'comprehension_wrong_attempts'
    player_number = 3
    players = ['Q', 'R', 'T', 'S', 'Unknown']
    colors = ['Purple','Green','Yellow','Unknown']
    questions = [
        {
            'question': 'What is your maximum payoff in each round?',
            'options': random.sample([20, 12, 6, 28, 'Unknown'], 5),
            'correct': 12,
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which player are you?',
            'options': random.sample(players, 5),
            'correct': players[player_number],
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Whose payoffs are shown to you at the end of each round?',
            'options': random.sample({'Only your own', "Nobody's", "Everyone's", "Your own and those of players adjacent to you"}, 4),
            'correct': 'Only your own',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player Q choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please see diagram above and instructions below.'
        },
        {
            'question': 'Which color did Player R choose?',
            'options': random.sample(colors, 4),
            'correct': 'Unknown',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player S choose?',
            'options': random.sample(colors, 4),
            'correct': 'Purple',
            'hint': 'Please review instructions below.'
        },
        {
            'question': 'Which color did Player T choose?',
            'options': random.sample(colors, 4),
            'correct': 'Green',
            'hint': 'Please review instructions below.'
        },
    ]

page_sequence = [MyWaitPage, Introduction, Q, R, S, T]