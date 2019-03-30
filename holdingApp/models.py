from django.db import models
from creationApp.models import Puzzle
import random


class Member(models.Model):
    team = models.ForeignKey('preparationApp.Team', models.CASCADE)
    quest = models.ForeignKey('preparationApp.Quest', models.CASCADE)
    current_puzzle = models.ForeignKey('creationApp.Puzzle', models.SET_DEFAULT, default=1)
    puzzle_start = models.DateTimeField(auto_now_add=True)

    def give_puzzle(self):
        if self.quest.free_puzzles():
            self.current_puzzle = random.choice(self.quest.free_puzzles())
            self.save()
        else:
            self.current_puzzle = random.choice(list(filter(lambda p: p.quest == self.quest, Puzzle.objects.all())))
            self.save()

    class Meta:
        unique_together = (("team", "quest"),)
