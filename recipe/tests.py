from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name="Test Recipe", year=2023)
        self.recipe_detail_url = reverse('recipe_detail', args=[self.recipe.id])

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.recipe.name)

    def test_recipe_detail_view(self):
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        self.assertContains(response, self.recipe.name)
        self.assertContains(response, self.recipe.year)
