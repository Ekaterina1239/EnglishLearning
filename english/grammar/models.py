from django.db import models


class GrammarTopic(models.Model):
    class Level(models.TextChoices):
        A1 = "A1", "A1"; A2 = "A2", "A2"; B1 = "B1", "B1"; B2 = "B2", "B2"; C1 = "C1", "C1"

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    level = models.CharField(max_length=2, choices=Level.choices, default=Level.A1)
    explanation = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return f"{self.title} ({self.level})"


class GrammarExample(models.Model):
    topic = models.ForeignKey(GrammarTopic, on_delete=models.CASCADE, related_name="examples")
    sentence_en = models.CharField(max_length=500)
    sentence_translation = models.CharField(max_length=500, blank=True)
    note = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.sentence_en