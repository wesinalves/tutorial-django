from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("question/add/", views.QuestionCreateView.as_view(), name="question-add"),
    path("question/<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question-delete"),
    path("question/<int:pk>/update/", views.QuestionUpdateView.as_view(), name="question-update"),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results", views.ResultsView.as_view(), name='results'),
    path("<int:question_id>/vote", views.vote, name='vote'),

    path("choice/add/", views.ChoiceCreateView.as_view(), name="choice-add"),
    path("choice/<int:pk>/", views.ChoiceDetail.as_view(), name="choice-detail"),
    path("choice/<int:pk>/delete/", views.ChoiceDeleteView.as_view(), name="choice-delete"),
]