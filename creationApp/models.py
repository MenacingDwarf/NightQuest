from django.db import models
from preparationApp.models import Quest


class Puzzle(models.Model):
    quest = models.ForeignKey(Quest, models.CASCADE)
    title = models.CharField(max_length=50)
    html = models.TextField()
    auto_skip_minutes = models.IntegerField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    puzzle = models.ForeignKey(Puzzle, models.CASCADE)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value


class Hint(models.Model):
    puzzle = models.ForeignKey(Puzzle, models.CASCADE)
    fine_minutes = models.IntegerField()
    open_minutes = models.IntegerField()
    html = models.TextField()

    def __str__(self):
        return self.html
