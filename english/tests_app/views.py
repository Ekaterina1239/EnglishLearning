import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Test, TestAttempt


def test_detail(request, slug):
    test = get_object_or_404(Test, slug=slug)
    questions = test.questions.prefetch_related('choices')
    return render(request, 'tests_app/detail.html', {'test': test, 'questions': questions})


@login_required
def test_submit(request, slug):
    """
    Обрабатывает отправку теста через HTMX (POST), возвращает готовый
    HTML-фрагмент с результатом — без перезагрузки страницы.
    """
    test = get_object_or_404(Test, slug=slug)
    questions = list(test.questions.prefetch_related('choices'))

    correct_count = 0
    for question in questions:
        selected_id = request.POST.get(f'question_{question.id}')
        if selected_id:
            correct_choice = question.choices.filter(is_correct=True).first()
            if correct_choice and str(correct_choice.id) == selected_id:
                correct_count += 1

    total = len(questions)
    score_percent = round((correct_count / total) * 100) if total else 0

    TestAttempt.objects.create(
        user=request.user,
        test=test,
        score_percent=score_percent,
        completed_at=timezone.now(),
    )

    return render(request, 'tests_app/result.html', {
        'test': test,
        'correct_count': correct_count,
        'total': total,
        'score_percent': score_percent,
    })