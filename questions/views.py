from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required



def home(request):
    if request.user.is_authenticated:
        courses = Course.objects.all()
        context = {'courses': courses}
        return render(request, 'quest/home.html', context)
    else:
        return redirect('login_attempt')


def api_question(request, id):
    if request.user.is_authenticated:
        raw_questions = Question.objects.filter(course=id)[:20]
        questions = []

        for raw_question in raw_questions:
            question = {}
            question['id'] = raw_question.id
            question['question'] = raw_question.question
            question['answer'] = raw_question.answer
            question['marks'] = raw_question.marks
            options = []
            options.append(raw_question.option_one)
            options.append(raw_question.option_two)
            if raw_question.option_three != '':
                options.append(raw_question.option_three)

            if raw_question.option_four != '':
                options.append(raw_question.option_four)

            question['options'] = options

            questions.append(question)

        return JsonResponse(questions, safe=False)
    else:
        return redirect('login_attempt')


def view_score(request):
    if request.user.is_authenticated:
        user = request.user
        score = ScoreBoard.objects.filter(user=user)
        context = {'score': score}
        return render(request, 'quest/score.html', context)
    else:
        return redirect('login_attempt')



def take_quiz(request, id):
    if request.user.is_authenticated:
        context = {'id': id}
        return render(request, 'quest/quiz.html', context)
    else:
        return redirect('login_attempt')


@csrf_exempt
def check_score(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        user = request.user
        course_id = data.get('course_id')
        solutions = json.loads(data.get('data'))
        course = Course.objects.get(id=course_id)
        score = 0
        for solution in solutions:
            question = Question.objects.filter(id=solution.get('question_id')).first()

            if (question.answer) == solution.get('option'):
                score = score + question.marks

        score_board = ScoreBoard(course=course, score=score, user=user)
        score_board.save()

        return JsonResponse({'message': 'success', 'status': True})
    else:
        return redirect('login_attempt')

