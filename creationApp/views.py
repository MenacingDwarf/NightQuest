from django.shortcuts import render, redirect
from preparationApp.models import Quest
from .models import Puzzle,Hint,Answer


def get_args(quest_id):
    quest = Quest.objects.get(id=quest_id)
    puzzles = list(filter(lambda p: p.quest == quest, Puzzle.objects.all()))
    return {'quest': quest, 'puzzles': puzzles}


def main_edit(request, quest_id):
    if request.method == 'POST':
        quest = Quest.objects.get(id=quest_id)
        quest.title = request.POST['title']
        quest.description = request.POST['description']
        quest.save()
        return redirect('/edit/'+str(quest_id))
    else:
        return render(request, 'creationApp/mainEditPage.html', get_args(quest_id))


def add_puzzle(request, quest_id):
    puzzle = Puzzle(quest=Quest.objects.get(id=quest_id), title=request.POST['title'],
                    html=request.POST['html'], auto_skip_minutes=request.POST['auto_skip_minutes'])
    puzzle.save()
    return redirect('/edit/'+str(quest_id))


def edit_puzzle(request, quest_id):
    puzzle = Puzzle.objects.get(id=int(request.POST['id']))
    puzzle.title = request.POST['title']
    puzzle.html = request.POST['html']
    puzzle.auto_skip_minutes = request.POST['auto_skip_minutes']
    puzzle.save()
    return redirect('/edit/'+str(quest_id)+'/puzzle/'+str(request.POST['id']))


def puzzle_page(request, quest_id, puzzle_id):
    args = get_args(quest_id)
    args['puzzle'] = Puzzle.objects.get(id=puzzle_id)
    print(args)
    return render(request, 'creationApp/puzzlePage.html', args)
