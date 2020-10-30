from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="",
    keywords='bonus, study',
    title='Title for your experiment',
    description='Description for your experiment',
    frame_height=500,
    template='global/mturk_template.html',
    minutes_allotted_per_assignment=60,
    expiration_hours=7 * 24,
    qualification_requirements=[]
    #grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
)


SESSION_CONFIGS = [
    dict(
        name='line',
        display_name="Line",
        num_demo_participants=4,
        app_sequence=['survey','line_instruc_comprehen_set1','line_set1'
                      ],
    )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree']