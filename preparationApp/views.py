from django.shortcuts import render, redirect
from django.utils import timezone
from . import models
from django.contrib.auth.models import User
from holdingApp.models import Member
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from datetime import datetime

def test(request):
    return render(request, 'frontend/index.html')

def get_user(name):
    return User.objects.get(username=name)


def make_args(request):
    args = {'message': 'none'}
    if request.session.get('message'):
        args['message'] = request.session.get('message')
        request.session.pop('message')
    return args


def main_page(request):
    return render(request, 'frontend/index.html', make_args(request))

@csrf_exempt
def log_in(request):
    if request.method == 'GET':
        args = make_args(request)
        return render(request, 'frontend/index.html', args)
    else:
        try:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                print('login', request.POST['username'])
                login(request, user)
                return redirect('/')
            else:
                request.session['message'] = 'Неверный пароль'
                return redirect('/login/')
        except ValueError:
            request.session['message'] = 'Пользователь не зарегистрирован'
            return redirect('/login/')

@csrf_exempt
def register(request):
    if request.method == 'GET':
        args = make_args(request)
        return render(request, 'frontend/index.html', args)
    else:
        try:
            user = User.objects.get(username=request.POST['username'])
            request.session['message'] = 'Пользователь уже зарегистрирован'
            return redirect('/register/')
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            login(request, user)
            print('register', request.POST['username'])
            return redirect('/')


def get_user_info(request):
    if request.user.is_authenticated:
        return JsonResponse({"is_auth": True, "user_info": model_to_dict(request.user)})
    else:
        return JsonResponse({"is_auth": False})


def personal_area(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            args = make_args(request)
            return render(request, 'preparationApp/personalPage.html', args)
        else:
            user = get_user(request.user.username)
            user.first_name = request.POST['f_name']
            user.last_name = request.POST['l_name']
            user.email = request.POST['email']
            user.save()
            request.session['message'] = 'Изменения были сохранены'
            return redirect('/personal/')
    else:
        return redirect('/login')


def teams(request):
    if request.user.is_authenticated:
        args = make_args(request)
        args['teams_list'] = list(filter(lambda t: get_user(request.user.username) in t.members.all(),
                                         models.Team.objects.all()))

        args['invites_list'] = list(filter(lambda i: get_user(request.user.username) == i.new_member,
                                           models.Invite.objects.all()))

        return render(request, 'preparationApp/teamsPage.html', args)
    else:
        request.session['message'] = 'Необходима авторизация'
        return redirect('/login')


def team_info(request, team_id):
    args = make_args(request)
    item = models.Team.objects.get(id=team_id)
    args['team'] = {'id': team_id, 'title': item.title,
                    'captain': str(item.captain),
                    'members': list(map(str, item.members.all()))}
    return render(request, 'preparationApp/teamInfoPage.html', args)


def change_team(request):
    team = models.Team.objects.get(id=int(request.POST['team_id']))
    team.title = request.POST['title']
    for member in team.members.all():
        if request.POST.get(str(member)):
            team.members.remove(member)
    team.captain = User.objects.get(username=request.POST['captain'])
    team.save()
    request.session['message'] = 'Изменения были сохранены'
    return redirect('/teams')


def add_team(request):
    team = models.Team(captain=get_user(request.user.username), title=request.POST['title'])
    team.save()
    team.members.add(get_user(request.user.username))
    team.save()
    request.session['message'] = 'Команда была создана'
    return redirect('/teams')


def add_member(request):
    invite = models.Invite(new_member=get_user(request.POST['new_member']),
                           team=models.Team.objects.get(id=request.POST['team_id']))
    invite.save()
    request.session['message'] = 'Приглашение участнику отправлено'
    return redirect('/teams')


def leave_team(request, team_id):
    team = models.Team.objects.get(id=team_id)
    team.members.remove(get_user(request.user.username))
    return redirect('/teams')


def accept_invite(request, invite_id):
    invite = models.Invite.objects.get(id=invite_id)
    models.Team.objects.get(id=invite.team.id).members.add(get_user(request.user.username))
    invite.delete()
    return redirect('/teams')


def quests(request):
    args = make_args(request)
    args['your_quests'] = list(filter(lambda q: get_user(request.user.username) == q.owner,
                                      models.Quest.objects.all()))
    args['other_quests'] = list(filter(lambda q: get_user(request.user.username) != q.owner,
                                       models.Quest.objects.all()))
    return render(request, 'preparationApp/questsPage.html', args)


def quest_info(request, quest_id):
    args = make_args(request)
    args['quest'] = models.Quest.objects.get(id=quest_id)
    args['teams'] = list(filter(lambda t: User.objects.get(username=request.user.username) == t.captain,
                                models.Team.objects.all()))
    args['requests'] = list(filter(lambda r: models.Quest.objects.get(id=quest_id) == r.quest,
                                   models.Request.objects.all()))

    reg_teams = list(
        filter(lambda m: get_user(request.user.username) in m.team.members.all() and m.quest == args['quest'],
               Member.objects.all()))
    if not reg_teams:
        args['registered'] = False
    else:
        args['registered'] = reg_teams[0].team.title

    return render(request, 'preparationApp/questInfoPage.html', args)


def add_quest(request):
    if request.user.is_authenticated:
        print(request.POST['start_date'])
        quest = models.Quest(title=request.POST['title'], description=request.POST['description'],
                             owner=get_user(request.user.username),
                             start_date=timezone.datetime.strptime(request.POST['start_date'], "%Y-%m-%dT%H:%M"))
        quest.start_date -= timezone.timedelta(hours=3)
        quest.save()
        return redirect('/quests')
    else:
        request.session['message'] = 'Необходима авторизация'
        return redirect('/login')


def make_quest_request(request):
    req = models.Request(quest=models.Quest.objects.get(id=request.POST['id']),
                         team=models.Team.objects.get(id=int(request.POST['team'])))
    req.save()
    request.session['message'] = 'Заявка на участие отправлена'
    return redirect('/quests')


def submit_quest_request(request):
    req = models.Request.objects.get(id=int(request.POST['id']))
    member = Member(team=req.team, quest=req.quest, puzzle_start=req.quest.start_date)
    member.save()
    member.give_puzzle()
    member.save()
    req.delete()
    return redirect('/quests')


def log_out(request):
    logout(request)
    return redirect('/')
