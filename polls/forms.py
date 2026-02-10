from django.forms import ModelForm
from .models import Question, Choice
from django import forms

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
    
        widgets = {
            'question_text': forms.TextInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'pub_date': forms.DateInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', "type": "date"}),
        }

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'question']
    
        widgets = {
            'choice_text': forms.TextInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'question': forms.Select(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }