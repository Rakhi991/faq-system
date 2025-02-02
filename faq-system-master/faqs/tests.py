import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import FAQ

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def sample_faq():
    return FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )

@pytest.mark.django_db
class TestFAQAPI:
    def test_create_faq(self, api_client):
        url = reverse('faq-list')
        data = {
            'question': 'Test Question',
            'answer': 'Test Answer'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert FAQ.objects.count() == 1
        
    def test_list_faqs(self, api_client, sample_faq):
        url = reverse('faq-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        
    def test_get_faq_in_hindi(self, api_client, sample_faq):
        url = f"{reverse('faq-list')}?lang=hi"
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['question'] == sample_faq.question_hi
        
    def test_get_faq_in_bengali(self, api_client, sample_faq):
        url = f"{reverse('faq-list')}?lang=bn"
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]['question'] == sample_faq.question_bn

from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache
from .models import FAQ


class FAQTests(TestCase):
    """Test cases for FAQ functionality."""

    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.faq = FAQ.objects.create(
            question='Test Question?',
            answer='Test Answer',
            question_hi='टेस्ट प्रश्न?',
            answer_hi='टेस्ट उत्तर',
            question_bn='টেস্ট প্রশ্ন?',
            answer_bn='টেস্ট উত্তর'
        )

    def tearDown(self):
        """Clean up after tests."""
        cache.clear()

    def test_faq_creation(self):
        """Test FAQ model creation and fields."""
        self.assertEqual(self.faq.question, 'Test Question?')
        self.assertEqual(self.faq.answer, 'Test Answer')
        self.assertEqual(self.faq.question_hi, 'टेस्ट प्रश्न?')
        self.assertEqual(self.faq.answer_hi, 'टेस्ट उत्तर')
        self.assertEqual(self.faq.question_bn, 'টেস্ট প্রশ্ন?')
        self.assertEqual(self.faq.answer_bn, 'টেস্ট উত্তর')

    def test_faq_str_method(self):
        """Test FAQ string representation."""
        self.assertEqual(str(self.faq), 'Test Question?')

    def test_home_view(self):
        """Test home view with different languages."""
        # Test English (default)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Test Question?')

        # Test Hindi
        response = self.client.get(reverse('home') + '?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'टेस्ट प्रश्न?')

        # Test Bengali
        response = self.client.get(reverse('home') + '?lang=bn')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'টেস্ট প্রশ্ন?')

    def test_faq_caching(self):
        """Test FAQ caching functionality."""
        # First request should cache the result
        translated = self.faq.get_translated_fields('en')
        self.assertEqual(translated['question'], 'Test Question?')
        self.assertEqual(translated['answer'], 'Test Answer')

        # Check if data is cached
        cache_key = f'faq_{self.faq.pk}_en'
        cached_data = cache.get(cache_key)
        self.assertIsNotNone(cached_data)
        self.assertEqual(cached_data['question'], 'Test Question?')

        # Update FAQ
        self.faq.question = 'Updated Question?'
        self.faq.save()

        # Cache should be cleared
        cached_data = cache.get(cache_key)
        self.assertIsNone(cached_data)

    def test_translation_fields(self):
        """Test get_translated_fields method."""
        # Test English
        translated = self.faq.get_translated_fields('en')
        self.assertEqual(translated['question'], 'Test Question?')
        self.assertEqual(translated['answer'], 'Test Answer')

        # Test Hindi
        translated = self.faq.get_translated_fields('hi')
        self.assertEqual(translated['question'], 'टेस्ट प्रश्न?')
        self.assertEqual(translated['answer'], 'टेस्ट उत्तर')

        # Test Bengali
        translated = self.faq.get_translated_fields('bn')
        self.assertEqual(translated['question'], 'টেস্ট প্রশ্ন?')
        self.assertEqual(translated['answer'], 'টেস্ট উত্তর')

    def test_invalid_language(self):
        """Test behavior with invalid language code."""
        # Should fallback to English
        translated = self.faq.get_translated_fields('invalid')
        self.assertEqual(translated['question'], 'Test Question?')
        self.assertEqual(translated['answer'], 'Test Answer')
