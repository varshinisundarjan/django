# admin.py
from django.contrib import admin
from .models import Lesson, Question, Choice, Submission  # import your models

# ---------- Inline Classes ----------

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    fields = ('choice_text', 'votes')
    readonly_fields = ('votes',)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('question_text', 'pub_date')
    readonly_fields = ('pub_date',)

# ---------- Admin Classes ----------

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'choice_count')
    inlines = [ChoiceInline]

    def choice_count(self, obj):
        return obj.choices.count()
    choice_count.short_description = "Number of Choices"

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'question_count')
    inlines = [QuestionInline]

    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = "Number of Questions"

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'question', 'choice', 'submitted_at')
    list_filter = ('submitted_at',)
