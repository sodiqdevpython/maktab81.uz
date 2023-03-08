import csv
import io
from random import shuffle, sample
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Question, Answer, Result, QuizModel

def qiuz(request):
    quizs = QuizModel.objects.all()
    context = {
        'quizs': quizs
    }
    return render(request, 'quiz.html', context)


@login_required(login_url='login')
def quistion(request, pk):
    quistions = Question.objects.filter(quiz_id = pk)
    # quistions = (list(quistions))
    answers = Answer.objects.all()
    answers = list(answers)
    shuffle(answers)
    if request.method == "POST":
        correct = 0
        wrong = 0
        for q in quistions:
            if request.POST.get(q.name) == "True":
                correct += 1
            else:
                wrong += 1
            quiz = q.quiz
        Result.objects.create(
            user=User.objects.get(username=request.user.username),
            total_question=len(quistions),
            corrent_question=correct,
            quiz = quiz
        )
        context = {
            'correct': correct,
            'wrong': wrong,
            'total_question': len(quistions),
            'user': set(request.user.username),
            'total': round(correct * 100 / len(quistions), 2),
        }
        return render(request, 'result.html', context)
    context = {
        'quistions': quistions,
        'answers': answers,
    }

    return render(request, 'quistion.html', context)


# def result_detail(request, result_id):
#     result_subject = Result.objects.all()
#     context = {
#         'result_subject': result_subject
#     }
#     # results = Result.objects.all().order_by('-corrent_question')
#     return render(request, 'detail_result_list.html', context)

#
# def list_result_view(request, pk):
#     result_detail = Result.objects.get(pk=pk)
#     return render(request, 'detail_result_list.html', {'result_detail': result_detail, 'pk': pk})

def result_list(request, pk):
    results_base = Result.objects.filter(quiz_id = pk).order_by('-corrent_question')
    context = {
        'results_base': results_base
    }
    return render(request, 'result_detail.html', context)