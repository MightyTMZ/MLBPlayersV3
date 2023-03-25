from django.db import models

# each team class is used to create a player for their team in the admin

AL = 'AL'
NL = 'NL'
al_east = 'AL East'
al_central = 'AL Central'
al_west = 'AL West'
nl_east = 'NL East'
nl_central = 'NL Central'
nl_west = 'NL West'

SP = 'SP'
RHP = 'RHP'
LHP = 'LHP'
first_baseman = '1B'
second_baseman = '2B'
SS = 'SS'
third_baseman = '3B'
RF = 'RF'
CF = 'CF'
LF = 'LF'
DH = 'DH'
C = 'C'

positions = [
    (SP, 'SP'),
    (RHP, 'RHP'),
    (LHP, 'LHP'),
    (first_baseman, '1B'),
    (second_baseman, '2B'),
    (SS, 'SS'),
    (third_baseman, '3B'),
    (RF, 'RF'),
    (CF, 'CF'),
    (LF, 'LF'),
    (DH, 'DH'),
    (C, 'C')
]


class Arizona_Diamondback(models.Model):
    name = models.CharField(max_length=255)
    team = 'Arizona Diamondbacks'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'arizona-diamondbacks'  # do not change


class Atlanta_Brave(models.Model):
    name = models.CharField(max_length=255)
    team = 'Atlanta Braves'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'atlanta-braves'  # do not change


class Baltimore_Oriole(models.Model):
    name = models.CharField(max_length=255)
    team = 'Baltimore Orioles'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'baltimore-orioles'  # do not change


class Boston_Red_Sox(models.Model):
    name = models.CharField(max_length=255)
    team = 'Boston Red Sox'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'boston-red-sox'


class Chicago_White_Sox(models.Model):
    name = models.CharField(max_length=255)
    team = 'Chicago White Sox'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'chicago-white-sox'


class Chicago_Cub(models.Model):
    name = models.CharField(max_length=255)
    team = 'Chicago Cubs'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'chicago-cubs'


class Cincinnati_Red(models.Model):
    name = models.CharField(max_length=255)
    team = 'Cincinnati Reds'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'cincinnati-reds'


class Cleveland_Guardian(models.Model):
    name = models.CharField(max_length=255)
    team = 'Cleveland Guardians'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'cleveland-guardians'


class Colorado_Rockie(models.Model):
    name = models.CharField(max_length=255)
    team = 'Colorado Rockies'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'colorado-rockies'


class Detroit_Tiger(models.Model):
    name = models.CharField(max_length=255)
    team = 'Detroit Tigers'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'detroit-tigers'


class Houston_Astro(models.Model):
    name = models.CharField(max_length=255)
    team = 'Houston Astros'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'houston-astros'


class Kansas_City_Royal(models.Model):
    name = models.CharField(max_length=255)
    team = 'Kansas City Royals'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'kansas-city-royals'


class Los_Angeles_Angel(models.Model):
    name = models.CharField(max_length=255)
    team = 'Los Angeles Angels'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'los-angeles-angels'


class Los_Angeles_Dodger(models.Model):
    name = models.CharField(max_length=255)
    team = 'Los Angeles Dodgers'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'los-angeles-dodgers'


class Miami_Marlin(models.Model):
    name = models.CharField(max_length=255)
    team = 'Miami Marlins'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'miami-marlins'


class Milwaukee_Brewer(models.Model):
    name = models.CharField(max_length=255)
    team = 'Milwaukee Brewers'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'milwaukee-brewers'


class Minnesota_Twin(models.Model):
    name = models.CharField(max_length=255)
    team = 'Minnesota Twins'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'minnesota-twins'


class New_York_Yankee(models.Model):
    name = models.CharField(max_length=255)
    team = 'New York Yankees'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'new-york-yankees'


class New_York_Met(models.Model):
    name = models.CharField(max_length=255)
    team = 'New York Mets'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'new-york-mets'


class Oakland_Athletic(models.Model):
    name = models.CharField(max_length=255)
    team = 'Oakland Athletics'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'oakland-athletics'


class Philadelphia_Phillie(models.Model):
    name = models.CharField(max_length=255)
    team = 'Philadelphia Phillies'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'philadelhia-phillies'


class Pittsburgh_Pirate(models.Model):
    name = models.CharField(max_length=255)
    team = 'Pittsburgh Pirates'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'pittsburgh-pirates'


class San_Diego_Padre(models.Model):
    name = models.CharField(max_length=255)
    team = 'San Diego Padres'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'san-diego-padres'


class San_Francisco_Giant(models.Model):
    name = models.CharField(max_length=255)
    team = 'San Francisco Giants'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'san-francisco-giants'


class Seattle_Mariner(models.Model):
    name = models.CharField(max_length=255)
    team = 'Seattle Mariners'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'seattle-mariners'


class St_Louis_Cardinal(models.Model):
    name = models.CharField(max_length=255)
    team = 'St. Louis Cardinals'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'st-louis-cardinals'


class Tampa_Bay_Ray(models.Model):
    name = models.CharField(max_length=255)
    team = 'Tampa Bay Rays'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'tampa-bay-rays'


class Texas_Ranger(models.Model):
    name = models.CharField(max_length=255)
    team = 'Texas Rangers'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'texas-rangers'


class Toronto_Blue_Jay(models.Model):
    name = models.CharField(max_length=255)
    team = 'Toronto Blue Jays'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'toronto-blue-jays'


class Washington_National(models.Model):
    name = models.CharField(max_length=255)
    team = 'Washington Nationals'  # do not change
    position = models.CharField(max_length=3, choices=positions, default='--')
    img_url = models.CharField(max_length=2083)
    team_id = 'washington-nationals'
