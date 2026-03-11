# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Path for submitting exam answers
    path('submit/', views.submit, name='submit'),
    
    # Path for showing exam results for a specific user
    path('result/<str:user_name>/', views.show_exam_result, name='show_exam_result'),
]
