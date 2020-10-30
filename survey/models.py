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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    zerotoseven_choices = [[1, ''],
                   [2, ''], [3, ''],
                   [4, ''],
                   [5, ''], [6, ''],
                   [7, '']]
    zerotoseven_ints=[1,2,3,4,5,6,7]

    Autonomy_1_table = 'survey/Autonomy_1.html'
    Autonomy_2_table = 'survey/Autonomy_2.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(label='What is your age?', min=13, max=125)

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'],
                 ['Other','Other'], ['Prefer not to say','Prefer not to say']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    autgen_1_1 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I feel like I am free to decide for myself how to live my life.',
        widget=widgets.RadioSelect
    )

    autgen_1_2 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I feel pressured in my life.',
        widget=widgets.RadioSelect
    )

    autgen_1_3 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I generally feel free to express my ideas and opinions.',
        widget=widgets.RadioSelect
    )

    autgen_1_4 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='In my daily life, I frequently have to do what I am told.',
        widget=widgets.RadioSelect
    )

    autgen_1_5 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='People I interact with on a daily basis tend to take my feelings into consideration.',
        widget=widgets.RadioSelect
    )

    autgen_1_6 = models.IntegerField(
        choices=Constants.zerotoseven_ints, min=3, max=3,
        label='Please click three in order to show that you are paying attention.',
        widget=widgets.RadioSelect
    )

    autgen_1_7 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I feel like I can pretty much be myself in my daily situations.',
        widget=widgets.RadioSelect
    )

    autgen_1_8 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='There is not much opportunity for me to decide for myself how to do things in my daily life.',
        widget=widgets.RadioSelect
    )

    autgen_2_1 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='My decisions represent my most important values and feelings.',
        widget=widgets.RadioSelect
    )

    autgen_2_2 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I do things in order to avoid feeling badly about myself.',
        widget=widgets.RadioSelect
    )

    autgen_2_3 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I often reflect on why I react the way I do.',
        widget=widgets.RadioSelect
    )

    autgen_2_4 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I strongly identify with the things that I do.',
        widget=widgets.RadioSelect
    )

    autgen_2_5 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I do a lot of things to avoid feeling ashamed.',
        widget=widgets.RadioSelect
    )

    autgen_2_6 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='My actions are in line with who I really am.',
        widget=widgets.RadioSelect
    )

    autgen_2_7 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I stand behind the important decisions I make.',
        widget=widgets.RadioSelect
    )

    autgen_2_8 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='I do or pretend to believe certain things so that others will like me.',
        widget=widgets.RadioSelect
    )

    autgen_2_9 = models.IntegerField(
        choices=Constants.zerotoseven_ints,
        label='My decisions are guided by what I want or care about.',
        widget=widgets.RadioSelect
    )