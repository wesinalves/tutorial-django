from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import QuestionForm, ChoiceForm
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class QuestionCreateView(generic.edit.CreateView):
    model = Question
    form_class = QuestionForm

class QuestionUpdateView(generic.edit.UpdateView):
    model = Question
    form_class = QuestionForm

class QuestionDeleteView(generic.edit.DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')

class ChoiceCreateView(generic.edit.CreateView):
    model = Choice
    form_class = ChoiceForm

class ChoiceDetail(generic.DetailView):
    model = Choice
    template_name = 'polls/choice-detail.html'

class ChoiceDeleteView(generic.edit.DeleteView):
    model = Choice
    success_url = reverse_lazy('polls:index')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {   
                'question': question,
                'error_message': "Você não selecionou um opção"
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

