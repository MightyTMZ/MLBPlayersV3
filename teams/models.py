from django.db import models


AL = 'AL'
NL = 'NL'
al_east = 'AL East'
al_central = 'AL Central'
al_west = 'AL West'
nl_east = 'NL East'
nl_central = 'NL Central'
nl_west = 'NL West'


class Team(models.Model):
    name = models.CharField(max_length=255)

    MLB_LEAGUES = [
        (AL, 'AL'),
        (NL, 'NL')
    ]

    MLB_DIVISIONS = [
        (al_east, 'AL East'),
        (al_central, 'AL Central'),
        (al_west, 'AL West'),
        (nl_east, 'NL East'),
        (nl_central, 'NL Central'),
        (nl_west, 'NL West')
    ]
    league = models.CharField(max_length=255, choices=MLB_LEAGUES, default='--')
    division = models.CharField(max_length=255, choices=MLB_DIVISIONS, default='--')
    img_url = models.ImageField(upload_to='teams/media/images')
    identification = models.CharField(max_length=255)