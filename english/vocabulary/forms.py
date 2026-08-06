from django import forms
from .models import VocabularySet, Word


class VocabularySetForm(forms.ModelForm):
    class Meta:
        model = VocabularySet
        fields = ["title", "slug", "description"]


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ["word_en", "translation", "transcription", "example_sentence"]