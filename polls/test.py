import datetime
from django.utils import timezone
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from polls.models import *

def create_question(question_text, days):
    
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() + datetime.timedelta(days=-30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)


    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(hours=-1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


class QuestionViewTests(TestCase):
    
    def test_index_view_with_no_question(self):
        #create_question('What flowers are you like', -2)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200 )
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual( response.context['latest_question_list'], [ ] )


class QuestionIndexDetailTests(TestCase):
    
    def test_detail_view_with_a_future_question(self):
        future_question = create_question(question_text='Future question.',
                                          days=5)
        response = self.client.get(reverse('polls:detail',
                                   args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)



 
