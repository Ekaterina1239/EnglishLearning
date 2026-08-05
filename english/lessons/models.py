from django.conf import settings
from django.db import models

from grammar.models import GrammarTopic
from reading.models import ReadingText
from tests_app.models import Test


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    order = models.PositiveIntegerField(default=0)

    grammar_topic = models.ForeignKey(GrammarTopic, on_delete=models.SET_NULL, null=True, blank=True, related_name="lessons")
    reading_text = models.ForeignKey(ReadingText, on_delete=models.SET_NULL, null=True, blank=True, related_name="lessons")
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, blank=True, related_name="lessons")

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lesson_progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="progress_entries")
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "lesson")
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.user} — {self.lesson}"