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
    test = get_object_or_404(Test, slug=slug)
    questions = list(test.questions.prefetch_related('choices'))

    correct_count = 0
    wrong_answers = []
    for question in questions:
        selected_id = request.POST.get(f'question_{question.id}')
        correct_choice = question.choices.filter(is_correct=True).first()

        if selected_id and correct_choice and str(correct_choice.id) == selected_id:
            correct_count += 1
        elif correct_choice:
            chosen_choice = question.choices.filter(id=selected_id).first()
            wrong_answers.append({
                "question": question.text,
                "category": question.category,
                "chosen": chosen_choice.text if chosen_choice else "(no answer)",
                "chosen_explanation": chosen_choice.explanation if chosen_choice else "",
                "correct": correct_choice.text,
            })

    total = len(questions)
    score_percent = round((correct_count / total) * 100) if total else 0

    TestAttempt.objects.create(
        user=request.user, test=test, score_percent=score_percent, completed_at=timezone.now(),
    )

    lesson = test.lessons.first()
    lesson_completed = False
    if lesson and score_percent >= 60:
        from lessons.models import LessonProgress
        LessonProgress.objects.update_or_create(
            user=request.user, lesson=lesson,
            defaults={'is_completed': True, 'completed_at': timezone.now()},
        )
        lesson_completed = True

    request.session['last_wrong_answers'] = wrong_answers

    return render(request, 'tests_app/result.html', {
        'test': test, 'correct_count': correct_count, 'total': total,
        'score_percent': score_percent, 'lesson': lesson,
        'lesson_completed': lesson_completed, 'has_mistakes': bool(wrong_answers),
    })