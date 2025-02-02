from django.db import models
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
import html
import time

class FAQ(models.Model):
    """FAQ model with multilingual support."""
    question = models.CharField(max_length=200)
    answer = RichTextField()
    question_hi = models.CharField(max_length=200, blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.CharField(max_length=200, blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        """Save FAQ and clear cache."""
        # Clear cache before saving
        if self.pk:
            self._clear_cache()
        super().save(*args, **kwargs)

    def _clear_cache(self):
        """Clear FAQ cache."""
        for lang in ['en', 'hi', 'bn']:
            cache.delete(f'faq_{self.pk}_{lang}')

    def get_translated_fields(self, lang):
        """Get translated fields based on language."""
        cache_key = f'faq_{self.pk}_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        if lang == 'hi':
            data = {
                'question': self.question_hi or self.question,
                'answer': self.answer_hi or self.answer
            }
        elif lang == 'bn':
            data = {
                'question': self.question_bn or self.question,
                'answer': self.answer_bn or self.answer
            }
        else:
            data = {
                'question': self.question,
                'answer': self.answer
            }

        cache.set(cache_key, data, 3600)  # Cache for 1 hour
        return data
