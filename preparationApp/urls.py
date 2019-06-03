from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('test/', views.test, name="test"),
    path('login/', views.log_in, name='log_in'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('personal/', views.personal_area, name='personal'),
    path('user_info', views.get_user_info, name="user_info"),

    path('teams', views.teams, name='teams'),
    path('teams/<int:team_id>', views.team_info, name='team_info'),
    path('teams/change', views.change_team, name='change_team'),
    path('teams/add/member', views.add_member, name='add_member'),
    path('teams/add/team', views.add_team, name='add_team'),
    path('teams/<int:team_id>/leave', views.leave_team, name='leave_team'),
    path('teams/accept/invite/<int:invite_id>', views.accept_invite, name='accept_invite'),

    path('quests', views.quests, name='quests'),
    path('quests/<int:quest_id>', views.quest_info, name='quest_info'),
    path('quests/add', views.add_quest, name='add_quest'),
    path('quests/request', views.make_quest_request, name='make_quest_request'),
    path('quests/submit', views.submit_quest_request, name='submit_quest_request')
]
