from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rango.models import Category

# Model test
class CategoryMethodTests(TestCase):
    def test_slug_line_creation(self):
        """
        Checks to make sure that when a category is created, an
        appropriate slug is created.
        """
        category = Category(name='Random Category String')
        category.save()

        self.assertEqual(category.slug, 'random-category-string')

# this function is for test the add category
def add_category(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.save()
    return category


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        '''
        If no categories exist, the appropriate message should be displayed
        '''

        response = self.client.get(reverse('rango:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categorylist(self):
        """
        Checks whether categories are displayed correctly when present
        """
        add_category('Crime')
        add_category('Fantasy')
        add_category('History')

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Crime")
        self.assertContains(response, "Fantasy")
        self.assertContains(response, "History")

        num_category = len(response.context['categorylist'])
        self.assertEquals(num_category, 3)
