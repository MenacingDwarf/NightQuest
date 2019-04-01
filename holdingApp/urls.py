from django.urls import path
from . import views

urlpatterns = [
    path('<int:quest_id>', views.current_puzzle, name="current_puzzle"),
    path('<int:quest_id>/check_code', views.check_code, name="check_code")
]
