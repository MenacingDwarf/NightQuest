from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from preparationApp.models import Quest
from creationApp.models import Answer
from .models import Member


def make_args(request):
    args = {'message': 'none'}
    if request.session.get('message'):
        args['message'] = request.session.get('message')
        request.session.pop('message')
    return args


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


def get_answers(user_id, quest_id):
    member = get_member(user_id, quest_id)
    answers = []
    for answer in list(filter(lambda a: a.puzzle == member.current_puzzle, Answer.objects.all())):
        if answer in member.answers.all():
            answers.append(answer.value)
        else:
            answers.append('none')
    return answers


def next_puzzle(user_id, quest_id):
    member = get_member(user_id, quest_id)
    member.puzzles.add(member.current_puzzle)
    member.give_puzzle()
    member.puzzle_start = timezone.now()
    member.save()


def current_puzzle(request, quest_id):
    if get_member(request.user.id, quest_id) is None:
        request.session['message'] = 'Пользователь не зарегистрирован на квест'
        return redirect('/')
    else:
        member = get_member(request.user.id, quest_id)
        args = make_args(request)
        args['time_left'] = parse_date(member.puzzle_start + timezone.timedelta(hours=2) - timezone.now())
        print(args['time_left'])
        if args['time_left'] == 'past':
            next_puzzle(request.user.id, quest_id)

        args['to_quest'] = parse_date(Quest.objects.get(id=quest_id).start_date - timezone.now())
        args['quest'] = Quest.objects.get(id=quest_id)
        args['complete'] = member.complete
        args['puzzle'] = member.current_puzzle
        args['answers'] = get_answers(request.user.id, quest_id)

        return render(request, 'holdingApp/currentPuzzlePage.html', args)


def check_code(request, quest_id):
    member = get_member(request.user.id, quest_id)
    request.session['message'] = 'wrong'
    answers = list(filter(lambda a: a.puzzle == member.current_puzzle, Answer.objects.all()))
    for ans in answers:
        if ans.value == request.POST['code']:
            member.answers.add(ans)
            member.save()
            request.session['message'] = 'right'
    if len(list(filter(lambda a: a.puzzle == member.current_puzzle, member.answers.all()))) == len(answers):
        next_puzzle(request.user.id, quest_id)
    return redirect('/quest/'+str(quest_id))
