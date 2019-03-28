from django.urls import path
from . import views

urlpatterns = [
    path('<int:quest_id>', views.main_edit, name="main_edit"),
    path('<int:quest_id>/add/puzzle', views.add_puzzle, name="add_puzzle"),
    path('<int:quest_id>/edit/puzzle', views.edit_puzzle, name="edit_puzzle"),
    path('<int:quest_id>/puzzle/<int:puzzle_id>', views.puzzle_page, name="puzzle_page")
]
