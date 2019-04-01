from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from preparationApp.models import Quest, Team
from .models import Member


def parse_date(timedelta):
    if timedelta.days < 0:
        return 'past'
    else:
        days = int(timedelta.days)
        hours = (timedelta.seconds - days * 24) // 3600
        minutes = (timedelta.seconds - days * 24 - hours * 3600) // 60
        seconds = timedelta.seconds - days * 24 - hours * 3600 - minutes * 60
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}


def get_member(user_id, quest_id):
    members = list(filter(
        lambda m: User.objects.get(id=user_id) in m.team.members.all() and m.quest == Quest.objects.get(id=quest_id),
        Member.objects.all()))
    return members[0] if members else None


def current_puzzle(request, quest_id):
    if get_member(request.user.id, quest_id) is None:
        request.session['message'] = 'Пользователь не зарегистрирован на квест'
        return redirect('/')
    else:
        member = get_member(request.user.id, quest_id)
        print(member.puzzle_start, timezone.now() + timezone.timedelta(hours=3))
        return render(request, 'holdingApp/currentPuzzlePage.html',
                      {'to_quest': parse_date(Quest.objects.get(id=quest_id).start_date - timezone.now()),
                       'quest': Quest.objects.get(id=quest_id),
                       'puzzle': member.current_puzzle,
                       'time_left': parse_date(member.puzzle_start + timezone.timedelta(hours=2) - timezone.now())})
