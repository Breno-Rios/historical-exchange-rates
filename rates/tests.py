#https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Server-side/Django/Testing
#https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/learn/lecture/29623186#overview
from django.test import TestCase

# Create your tests here.

class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1, 'Um é igual a um'
