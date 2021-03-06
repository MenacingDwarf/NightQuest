from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from preparationApp.models import Quest
from creationApp.models import Answer, Hint
from .models import Member


def make_args(request, quest_id):
    args = {'quest': Quest.objects.get(id=quest_id), 'message': 'none'}
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


def get_hints(user_id, quest_id):
    member = get_member(user_id, quest_id)
    hints = []
    for hint in list(filter(lambda h: h.puzzle == member.current_puzzle, Hint.objects.all())):
        item = {'id': hint.id, 'fine_minutes': hint.fine_minutes, 'html': hint.html,
                'open_time': parse_date(
                    member.puzzle_start + timezone.timedelta(minutes=hint.open_minutes) - timezone.now())}
        if hint in member.hints.all():
            item['used'] = True
        else:
            item['used'] = False
        hints.append(item)
    return hints


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
        args = make_args(request, quest_id)
        args['time_left'] = parse_date(member.puzzle_start + timezone.timedelta(hours=2) - timezone.now())
        if args['time_left'] == 'past':
            next_puzzle(request.user.id, quest_id)

        args['to_quest'] = parse_date(Quest.objects.get(id=quest_id).start_date - timezone.now())
        args['complete'] = member.complete
        args['puzzle'] = member.current_puzzle
        args['answers'] = get_answers(request.user.id, quest_id)
        args['hints'] = get_hints(request.user.id, quest_id)

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


def take_hint(request, quest_id):
    member = get_member(request.user.id, quest_id)
    member.hints.add(Hint.objects.get(id=request.POST['id']))
    member.save()
    return redirect('/quest/' + str(quest_id))


def get_statistic(request, quest_id):
    members = list(filter(lambda m: m.quest == Quest.objects.get(id=quest_id), Member.objects.all()))
    args = make_args(request, quest_id)
    args['members'] = []
    for member in members:
        time = timezone.now() - Quest.objects.get(id=quest_id).start_date
        item = {'team': member.team.title,
                'fine': sum([hint.fine_minutes for hint in member.hints.all()]),
                'time': parse_date(time),
                'puzzles': len(member.puzzles.all()),
                'puzzle': member.current_puzzle.title}
        item['time']['hours'] += item['time']['days'] * 24
        item['summary_time'] = parse_date(time + timezone.timedelta(minutes=item['fine']))
        item['summary_time']['hours'] += item['summary_time']['days'] * 24
        args['members'].append(item)

    return render(request, 'holdingApp/statisticPage.html', args)
