from django.urls import path
from . import views

urlpatterns = [
    path('<int:quest_id>', views.main_edit, name="main_edit")
]
