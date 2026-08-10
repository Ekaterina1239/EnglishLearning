from django.conf import settings
from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Question(models.Model):
    class Category(models.TextChoices):
        VERB_TENSE = "verb_tense", "Verb tense"
        ARTICLES = "articles", "Articles (a/an/the)"
        PREPOSITIONS = "prepositions", "Prepositions"
        SUBJECT_VERB = "subject_verb", "Subject-verb agreement"
        WORD_ORDER = "word_order", "Word order"
        VOCABULARY = "vocabulary", "Vocabulary / word choice"
        OTHER = "other", "Other"

    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=500)
    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.OTHER,
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    explanation = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.text


class TestAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="test_attempts")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="attempts")
    score_percent = models.PositiveSmallIntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.user} — {self.test} — {self.score_percent}%"