from django.contrib import admin
from . import models

admin.site.register(models.Puzzle)
admin.site.register(models.Answer)
admin.site.register(models.Hint)
