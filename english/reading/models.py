from django.db import models


class ReadingText(models.Model):
    class Level(models.TextChoices):
        A1 = "A1", "A1"; A2 = "A2", "A2"; B1 = "B1", "B1"; B2 = "B2", "B2"; C1 = "C1", "C1"

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    level = models.CharField(max_length=2, choices=Level.choices, default=Level.A1)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.level})"


class ComprehensionQuestion(models.Model):
    text = models.ForeignKey(ReadingText, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=300)
    wrong_answer_1 = models.CharField(max_length=300)
    wrong_answer_2 = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.question