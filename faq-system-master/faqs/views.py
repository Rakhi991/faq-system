from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing FAQs.
    Supports language selection via ?lang= query parameter.
    """
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    
    def get_serializer_context(self):
        """Add language preference to serializer context."""
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'en')
        return context

@cache_page(60 * 15)  # Cache for 15 minutes
def home(request):
    """Home view displaying FAQs."""
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()

    faq_list = []
    for faq in faqs:
        translated = faq.get_translated_fields(lang)
        faq_list.append({
            'id': faq.id,
            'question': translated['question'],
            'answer': translated['answer'],
            'created_at': faq.created_at
        })

    context = {
        'faqs': faq_list,
        'current_lang': lang
    }
    return render(request, 'home.html', context)
