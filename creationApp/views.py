from django.shortcuts import render
from preparationApp.models import Quest


def main_edit(request, quest_id):
    if request.method == 'POST':
        quest = Quest.objects.get(id=quest_id)
        quest.title = request.POST['title']
        quest.description = request.POST['description']
        quest.save()
    else:
        return render(request, 'creationApp/mainEditPage.html', {'quest': Quest.objects.get(id=quest_id)})
