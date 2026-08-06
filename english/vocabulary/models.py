from django.conf import settings
from django.db import models


class VocabularySet(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        null=True, blank=True, related_name="vocabulary_sets",
        help_text="Пусто = официальный набор (добавлен через /admin/). Заполнено = личный набор пользователя.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Word(models.Model):
    vocabulary_set = models.ForeignKey(VocabularySet, on_delete=models.CASCADE, related_name="words")
    word_en = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    example_sentence = models.CharField(max_length=500, blank=True)
    transcription = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["word_en"]

    def __str__(self):
        return f"{self.word_en} — {self.translation}"