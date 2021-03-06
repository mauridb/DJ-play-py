# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


POSITIONS = (
    ('GK', 'Goalkeeper'),
    ('CB', 'Center fullback'),
    ('SW', 'Sweeper'),
    ('LFB', 'Left fullback'),
    ('RFB', 'Right fullback'),
    ('WB', 'Wingback'),
    ('LM', 'Left midfield'),
    ('RM', 'Right midfield'),
    ('DM', 'Defensive midfield'),
    ('CM', 'Center midfield'),
    ('WM', 'Wide midfield'),
    ('CF', 'Center forward'),
    ('AM', 'Attacking midfield'),
    ('S', 'Striker'),
    ('SS', 'Second striker'),
    ('LW', 'Left winger'),
    ('RW', 'Right winger'),

)


class Team(models.Model):
    name = models.CharField(max_length=255)
    coach = models.ForeignKey(User, related_name='teams')
    practice_location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    position = models.CharField(choices=POSITIONS, max_length=3)
    team = models.ForeignKey(Team, related_name='players')

    def __str__(self):
        return self.name
