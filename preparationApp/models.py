from django.db import models
from django.contrib.auth.models import User
from holdingApp.models import Member
from creationApp.models import Puzzle
import random


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

    def all_puzzles(self):
        return list(filter(lambda p: p.quest == self, Puzzle.objects.all()))

    def free_puzzles(self):
        puzzles = []
        for puzzle in list(filter(lambda p: p.quest == self, Puzzle.objects.all())):
            if not list(filter(lambda m: m.current_puzzle == puzzle and m.quest == self, Member.objects.all())):
                puzzles.append(puzzle)
        return puzzles

    def give_puzzles(self):
        members = list(filter(lambda m: m.quest == self, Member.objects.all()))
        puzzles = list(filter(lambda p: p.quest == self, Puzzle.objects.all()))
        for member in members:
            if not puzzles:
                puzzles = list(filter(lambda p: p.quest == self, Puzzle.objects.all()))
            member.current_puzzle = random.choice(puzzles)
            puzzles.remove(member.current_puzzle)
            member.save()

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
