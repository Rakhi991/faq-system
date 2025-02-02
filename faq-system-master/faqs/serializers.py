from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    """
    Serializer for FAQ model with dynamic language support.
    """
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()
    
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']
        
    def get_question(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_translated_fields(lang)['question']
        
    def get_answer(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_translated_fields(lang)['answer']
