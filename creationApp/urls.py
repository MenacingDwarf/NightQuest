from django.urls import path
from . import views

urlpatterns = [
    path('<int:quest_id>', views.main_edit, name="main_edit"),
    path('<int:quest_id>/add/puzzle', views.add_puzzle, name="add_puzzle"),
    path('<int:quest_id>/edit/puzzle', views.edit_puzzle, name="edit_puzzle"),
    path('<int:quest_id>/delete/puzzle', views.delete_puzzle, name="delete_puzzle"),
    path('<int:quest_id>/puzzle/<int:puzzle_id>', views.puzzle_page, name="puzzle_page"),

    path('<int:quest_id>/edit/answers', views.edit_answers, name="edit_answers"),
    path('<int:quest_id>/add/answer', views.add_answer, name="add_answer"),
    path('<int:quest_id>/delete/answer/<int:answer_id>', views.delete_answer, name="delete_answer"),

    path('<int:quest_id>/add/hint', views.add_hint, name="add_hint"),
    path('<int:quest_id>/edit/hints', views.edit_hints, name="edit_hints"),
    path('<int:quest_id>/delete/hint/<int:hint_id>', views.delete_hint, name="delete_hint")
]
