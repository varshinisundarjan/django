# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice, Submission

# Function to submit exam answers
def submit(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        for question in Question.objects.all():
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                # Save submission
                Submission.objects.create(
                    user_name=user_name,
                    question=question,
                    choice=choice
                )
        return redirect('show_exam_result', user_name=user_name)

    # GET request - show form
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'exam/submit.html', context)

# Function to show exam result
def show_exam_result(request, user_name):
    submissions = Submission.objects.filter(user_name=user_name)
    total_questions = Question.objects.count()
    correct_answers = 0

    for submission in submissions:
        if submission.choice.id == submission.question.correct_choice.id:
            correct_answers += 1

    context = {
        'user_name': user_name,
        'submissions': submissions,
        'score': correct_answers,
        'total': total_questions
    }
    return render(request, 'exam/result.html', context)
