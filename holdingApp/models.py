from django.db import models
from creationApp.models import Puzzle
from django.utils import timezone
import random


class Member(models.Model):
    team = models.ForeignKey('preparationApp.Team', models.CASCADE)
    quest = models.ForeignKey('preparationApp.Quest', models.CASCADE)
    current_puzzle = models.ForeignKey('creationApp.Puzzle', models.SET_DEFAULT, default=1)
    puzzle_start = models.DateTimeField(default=timezone.now)
    answers = models.ManyToManyField('creationApp.Answer', related_name="users")
    hints = models.ManyToManyField('creationApp.Hint', related_name="users")

    def give_puzzle(self):
        if self.quest.free_puzzles():
            self.current_puzzle = random.choice(self.quest.free_puzzles())
            self.save()
        elif self.quest.all_puzzles():
            self.current_puzzle = random.choice(self.quest.all_puzzles())
            self.save()

    class Meta:
        unique_together = (("team", "quest"),)
