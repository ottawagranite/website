from django.core.exceptions import ValidationError


def team_is_all_male(team):
    if not all([p.gender == 'M' for p in team.players]):
        raise ValidationError('Team is not made of up all male players.')


def team_is_all_female(team):
    if not all([p.gender == 'F' for p in team.players]):
        raise ValidationError('Team is not made of up all female players.')


def team_is_mixed(team):
    genders = [p.gender for p in team.players]
    if not (genders.count('M') >= 2 and genders.count('F') >= 2):
        raise ValidationError('Team is not made of of all male players.')


league_formats = {
    "Men's Fixed": {'team_validators': [team_is_all_male, ]},
    "Women's Fixed": {'team_validators': [team_is_all_female, ]},
    "Mixed Fixed": {'team_validators': [team_is_mixed, ]},
    "Open Fixed": {'team_validators': []},
    "Men's Draw": {'team_validators': [team_is_all_male, ], },
    "Women's Draw": {'team_validators': [team_is_all_female, ]},
    "Mixed Draw": {'team_validators': [team_is_mixed, ]},
    "Open Draw": {'team_validators': []},
}
