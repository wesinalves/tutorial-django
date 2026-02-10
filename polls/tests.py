from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Question
# Create your tests here.

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

class QuestionIndexViewTest(TestCase):

    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "não há registros!")
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        create_question(question_text='future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'não há registros!')
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            [],
        )
    
    def test_future_and_past_question(self):
        question = create_question(question_text='past question', days=-30)
        create_question(question_text="future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            [question],
        )
    
    def test_two_past_question(self):
        question1 = create_question(question_text='past question', days=-30)
        question2 = create_question(question_text='past question', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )
        

