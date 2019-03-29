from django.shortcuts import render, redirect
from preparationApp.models import Quest
from .models import Puzzle,Hint,Answer


def get_args(quest_id):
    quest = Quest.objects.get(id=quest_id)
    puzzles = list(filter(lambda p: p.quest == quest, Puzzle.objects.all()))
    return {'quest': quest, 'puzzles': puzzles, 'message': 'none'}


def main_edit(request, quest_id):
    if request.method == 'POST':
        quest = Quest.objects.get(id=quest_id)
        quest.title = request.POST['title']
        quest.description = request.POST['description']
        quest.save()
        request.session['message'] = 'Информация о квесте была изменена'
        return redirect('/edit/'+str(quest_id))
    else:
        args = get_args(quest_id)
        if request.session.get('message'):
            args['message'] = request.session.get('message')
            request.session.pop('message')
        return render(request, 'creationApp/mainEditPage.html', args)


def add_puzzle(request, quest_id):
    puzzle = Puzzle(quest=Quest.objects.get(id=quest_id), title=request.POST['title'],
                    html=request.POST['html'], auto_skip_minutes=request.POST['auto_skip_minutes'])
    puzzle.save()
    request.session['message'] = 'Загадка была добавлена'
    return redirect('/edit/'+str(quest_id))


def edit_puzzle(request, quest_id):
    puzzle = Puzzle.objects.get(id=int(request.POST['id']))
    puzzle.title = request.POST['title']
    puzzle.html = request.POST['html']
    puzzle.auto_skip_minutes = request.POST['auto_skip_minutes']
    puzzle.save()
    request.session['message'] = 'Загадка была изменена'
    return redirect('/edit/'+str(quest_id)+'/puzzle/'+str(request.POST['id']))


def delete_puzzle(request, quest_id):
    puzzle = Puzzle.objects.get(id=request.POST['id'])
    puzzle.delete()
    request.session['message'] = 'Загадка была удалена'
    return redirect('/edit/' + str(quest_id))


def puzzle_page(request, quest_id, puzzle_id):
    args = get_args(quest_id)
    if request.session.get('message'):
        args['message'] = request.session.get('message')
        request.session.pop('message')
    args['puzzle'] = Puzzle.objects.get(id=puzzle_id)
    args['hints'] = list(filter(lambda h: h.puzzle == args['puzzle'], Hint.objects.all()))
    args['answers'] = list(filter(lambda a: a.puzzle == args['puzzle'], Answer.objects.all()))
    return render(request, 'creationApp/puzzlePage.html', args)


def add_answer(request, quest_id):
    answer = Answer(puzzle=Puzzle.objects.get(id=request.POST['id']), value=request.POST['answer'])
    answer.save()
    request.session['message'] = 'Ответ был добавлен'
    return redirect('/edit/'+str(quest_id)+'/puzzle/'+str(request.POST['id']), {'message': 'adding answer'})


def edit_answers(request, quest_id):
    for ans in (list(filter(lambda a: a.puzzle == Puzzle.objects.get(id=request.POST['id']), Answer.objects.all()))):
        ans.value = request.POST['answer'+str(ans.id)]
        ans.save()
    request.session['message'] = 'Ответы были изменены'
    return redirect('/edit/' + str(quest_id) + '/puzzle/' + str(request.POST['id']))


def delete_answer(request, quest_id, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.delete()
    request.session['message'] = 'Ответ был удалён'
    return redirect('/edit/' + str(quest_id) + '/puzzle/' + str(request.POST['id']))
