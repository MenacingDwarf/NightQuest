from django.db import models
from preparationApp.models import Quest, Team
from django.utils.timezone import now


class Member(models.Model):
    team = models.ForeignKey(Team, models.CASCADE)
    quest = models.ForeignKey(Quest, models.CASCADE)
    current_puzzle = models.IntegerField(default=1)
    puzzle_start = models.DateTimeField(default=now())

    class Meta:
        unique_together = (("team", "quest"),)
