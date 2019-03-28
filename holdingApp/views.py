from django.shortcuts import render, redirect
from datetime import datetime
from preparationApp.models import Quest


def current_puzzle(request, quest_id):
    return render(request, 'holdingApp/currentPuzzlePage.html',
                  {'current_time': datetime.utcnow(), 'quest': Quest.objects.get(id=quest_id)})
