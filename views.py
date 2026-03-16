from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        submission = Submission.objects.create(course=course)

        selected_choices = request.POST.getlist('choice')

        for choice_id in selected_choices:
            choice = Choice.objects.get(id=int(choice_id))
            submission.choices.add(choice)

        submission.save()

        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()
    selected_ids = [choice.id for choice in selected_choices]

    questions = Question.objects.filter(course=course)

    total_score = 0
    possible_score = 0

    for question in questions:
        possible_score += question.grade
        if question.is_get_score(selected_ids):
            total_score += question.grade

    context = {
        'course': course,
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
