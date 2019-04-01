from django.db import models
from creationApp.models import Puzzle
from django.utils import timezone
import random


class Member(models.Model):
    team = models.ForeignKey('preparationApp.Team', models.CASCADE)
    quest = models.ForeignKey('preparationApp.Quest', models.CASCADE)
    current_puzzle = models.ForeignKey('creationApp.Puzzle', models.SET_DEFAULT, default=1)
    puzzle_start = models.DateTimeField(default=timezone.now)
    answers = models.ManyToManyField('creationApp.Answer', related_name="members", null=True)
    hints = models.ManyToManyField('creationApp.Hint', related_name="members", null=True)
    puzzles = models.ManyToManyField('creationApp.Puzzle', related_name="members", null=True)
    complete = models.BooleanField(default=False)

    def give_puzzle(self):
        print(list(self.puzzles.all()), self.quest.all_puzzles())
        if list(self.puzzles.all()) == self.quest.all_puzzles():
            self.complete = True
        elif [p for p in self.quest.free_puzzles() if p not in list(self.puzzles.all())]:
            self.current_puzzle = random.choice([p for p in self.quest.free_puzzles() if p not in list(self.puzzles.all())])
            self.save()
        elif [p for p in self.quest.all_puzzles() if p not in list(self.puzzles.all())]:
            self.current_puzzle = random.choice([p for p in self.quest.all_puzzles() if p not in list(self.puzzles.all())])
            self.save()

    class Meta:
        unique_together = (("team", "quest"),)
