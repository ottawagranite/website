from curling.league_format import league_formats

PLAYER_GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

LEAGUE_FORMAT_CHOICES = [(x, x) for x in league_formats.keys()]

POSITION_CHOICES = (
    ('Lead', 'Lead'),
    ('Second', 'Second'),
    ('Third', 'Third'),
    ('Skip', 'Skip'),
    ('Alternate', 'Alternate'),
    ('Coach', 'Coach'),
    )
