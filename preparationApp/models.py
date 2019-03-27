from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Team(models.Model):
    captain = models.ForeignKey(User, models.CASCADE, default=1)
    members = models.ManyToManyField(User, related_name='teams')
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Quest(models.Model):
    title = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    description = models.TextField()
    owner = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.title


class Invite(models.Model):
    new_member = models.ForeignKey(User, models.CASCADE)
    team = models.ForeignKey(Team, models.CASCADE)

    class Meta:
        unique_together = (("new_member", "team"),)


class Request(models.Model):
    quest = models.ForeignKey(Quest, models.CASCADE)
    team = models.ForeignKey(Team, models.CASCADE)

    class Meta:
        unique_together = (("quest", "team"),)
