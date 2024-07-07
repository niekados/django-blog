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

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)