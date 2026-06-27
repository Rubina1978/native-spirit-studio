from django.test import TestCase
from .forms import ReflectionForm
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Reflection
# Create your tests here.


class TestReflectionForm(TestCase):

    def test_form_is_valid(self):
        reflection_form = ReflectionForm({
            'mood': 'Having a great Mood',
            'happy_moment': 'This is my happy moment',
            'gratitude': 'Im greatful',
            'challenge': 'this was very challenging',
            'notes': ''
        })
        self.assertTrue(reflection_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        reflection_form = ReflectionForm({
            'mood': '',
            'happy_moment': '',
            'gratitude': '',
            'challenge': '',
            'notes': ''
        })
        self.assertFalse(reflection_form.is_valid(), msg="form is valid")


class TestReflectionViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.reflection = Reflection.objects.create(
            user=self.user,
            mood="happy",
            happy_moment="sunny day",
            gratitude="almost at the end",
            challenge="testing",
            notes=""
        )

    def test_reflection_list_requires_login(self):
        response = self.client.get(reverse("journal"))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_see_reflections(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("journal"))

        self.assertEqual(response.status_code, 200)
