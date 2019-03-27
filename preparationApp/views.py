from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login


def get_user(name):
    return User.objects.get(username=name)


def main_page(request):
    return render(request, 'preparationApp/startPage.html')


def log_in(request):
    if request.method == 'GET':
        return render(request, 'preparationApp/loginPage.html')
    else:
        try:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                print('login', request.POST['username'])
                login(request, user)
                return redirect('/')
            else:
                return redirect('/login/')
        except ValueError:
            return redirect('/login/')


def register(request):
    if request.method == 'GET':
        return render(request, 'preparationApp/registerPage.html')
    else:
        try:
            user = User.objects.get(username=request.POST['username'])
            return redirect('login/')
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            login(request, user)
            print('register', request.POST['username'])
            return redirect('/')


def personal_area(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'preparationApp/personalPage.html')
        else:
            user = get_user(request.user.username)
            user.first_name = request.POST['f_name']
            user.last_name = request.POST['l_name']
            user.email = request.POST['email']
            user.save()
            return redirect('/personal/')
    else:
        return redirect('/login')


def teams(request):
    teams_list = list(filter(lambda t: User.objects.get(username=request.user.username) in t.members.all(),
                             models.Team.objects.all()))

    invites_list = list(filter(lambda i: User.objects.get(username=request.user.username) == i.new_member,
                               models.Invite.objects.all()))

    return render(request, 'preparationApp/teamsPage.html', {'teams_list': teams_list, 'invites_list': invites_list})


def team_info(request, team_id):
    item = models.Team.objects.get(id=team_id)
    team = {'id': team_id, 'title': item.title,
            'captain': str(item.captain),
            'members': list(map(str, item.members.all()))}
    return render(request, 'preparationApp/teamInfoPage.html', {'team': team})


def change_team(request):
    team = models.Team.objects.get(id=int(request.POST['team_id']))
    team.title = request.POST['title']
    for member in team.members.all():
        if request.POST.get(str(member)):
            team.members.remove(member)
    team.captain = User.objects.get(username=request.POST['captain'])
    team.save()
    return redirect('/teams')


def add_team(request):
    team = models.Team(captain=get_user(request.user.username), title=request.POST['title'])
    team.save()
    team.members.add(get_user(request.user.username))
    team.save()
    return redirect('/teams')


def add_member(request):
    invite = models.Invite(new_member=get_user(request.POST['new_member']),
                           team=models.Team.objects.get(id=request.POST['team_id']))
    invite.save()
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
    quests_list = models.Quest.objects.all()
    return render(request, 'preparationApp/questsPage.html', {'quests_list': quests_list})


def quest_info(request, quest_id):
    quest = models.Quest.objects.get(id=quest_id)
    teams_list = list(filter(lambda t: User.objects.get(username=request.user.username) == t.captain,
                             models.Team.objects.all()))
    requests_list = list(filter(lambda r: models.Quest.objects.get(id=quest_id) == r.quest,
                                models.Request.objects.all()))
    print(requests_list)

    return render(request, 'preparationApp/questInfoPage.html',
                  {'quest': quest, 'teams': teams_list, 'requests': requests_list})


def make_quest_request(request):
    req = models.Request(quest=models.Quest.objects.get(id=request.POST['id']),
                         team=models.Team.objects.get(id=int(request.POST['team'])))
    req.save()
    return redirect('/quests')


def log_out(request):
    logout(request)
    return redirect('/')
