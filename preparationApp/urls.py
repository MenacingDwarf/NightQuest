from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.log_in, name='log_in'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('personal/', views.personal_area, name='personal'),

    path('teams', views.teams, name='teams'),
    path('teams/<int:team_id>', views.team_info, name='team_info'),
    path('teams/change', views.change_team, name='change_team'),
    path('teams/add/member', views.add_member, name='add_member'),
    path('teams/<int:team_id>/leave', views.leave_team, name='leave_team'),
    path('teams/accept/invite/<int:invite_id>', views.accept_invite, name='accept_invite'),

    path('quests', views.quests, name='quests'),
    path('quests/<int:quest_id>', views.quest_info, name='quest_info')
]
