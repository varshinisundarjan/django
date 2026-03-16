from django.contrib import admin
from .models import Course, Lesson, Instructor, Question, Choice, Submission, Enrollment


class ChoiceInline(admin.InlineModelAdmin):
    model = Choice
    extra = 3


class QuestionInline(admin.InlineModelAdmin):
    model = Question
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'course', 'grade')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
