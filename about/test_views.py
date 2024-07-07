from django.test import TestCase
from django.urls import reverse
from .forms import CollaborateForm
from .models import About


class TestAboutViews(TestCase):
    """Test about vieews """

    def setUp(self):
        """Create about me content"""
        self.about_content = About(
            title = "tester",
            content = "test content"
        )
        self.about_content.save()

    def test_render_about_page_with_collaboration_form(self):
        """Verifies get request for about me containing 
        a collaboration form"""
        response = self.client.get(
            reverse('about')
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"tester", response.content)
        self.assertIn(b"test content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm
        )