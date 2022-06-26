from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import random 


@login_required(login_url='/auth/login')
def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    if request.GET.get('course'):
        return redirect(f"/quiz/?course={request.GET.get('course')}")

    return render(request, 'quest/home.html', context)

@login_required(login_url='/auth/login')
def quiz(request):
    courses = request.GET.get('course')
    context = {'course' : courses}
    return render (request, 'quest/quiz1.html', context)

@login_required(login_url='/auth/login')
def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('course'):
            question_objs = question_objs.filter(course__course_name__icontains=request.GET.get('course'))

        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            
            data.append({
                "uid" : question_obj.uid,
                "course" : question_obj.course.course_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers()
            })

        payload = {'status': True, 'data': data}

        return JsonResponse(payload)  
    except Exception as e:
        print (e)
    return HttpResponse("Algo deu errado!") 

@login_required(login_url='/auth/login')
def view_score(request):
    user = request.user
    score = ScoreBoard.objects.filter(user=user)
    context = {'score': score}
    return render(request, 'quest/score.html', context)



@login_required(login_url='/auth/login')
def take_quiz(request, uid):
    context = {'uid': uid}
    return render(request, 'quest/quiz.html', context)



@csrf_exempt
@login_required(login_url='/login')
def check_score(request):
    data = json.loads(request.body)
    user = request.user
    course_id = data.get('course_id')
    solutions = json.loads(data.get('data'))
    course = Course.objects.get(id=course_id)
    score = 0
    for solution in solutions:
        question = Question.objects.filter(id = solution.get('question_id')).first()
      
        if (question.answer) == solution.get('option'):
            score = score + question.marks
   
    score_board = ScoreBoard(course = course , score = score  , user = user)
    score_board.save() 
    
    return JsonResponse({'message' : 'success' , 'status':True})

