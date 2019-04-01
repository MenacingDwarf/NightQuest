from django.shortcuts import render, redirect
from django.utils import timezone
from preparationApp.models import Quest


def parse_date(timedelta):
    if timedelta.days < 0:
        return 'started'
    else:
        days = int(timedelta.days)
        hours = (timedelta.seconds - days * 24) // 3600
        minutes = (timedelta.seconds - days * 24 - hours * 3600) // 60
        seconds = timedelta.seconds - days * 24 - hours * 3600 - minutes * 60
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}


def current_puzzle(request, quest_id):
    print(Quest.objects.get(id=quest_id).start_date - timezone.now())
    return render(request, 'holdingApp/currentPuzzlePage.html',
                  {'to_quest': parse_date(Quest.objects.get(id=quest_id).start_date - timezone.now()),
                   'quest': Quest.objects.get(id=quest_id)})
