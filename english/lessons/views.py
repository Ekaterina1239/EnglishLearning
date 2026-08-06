from django.shortcuts import get_object_or_404, render
from .models import Lesson, LessonProgress


def lesson_list(request):
    lessons = Lesson.objects.all()

    completed_lesson_ids = set()
    if request.user.is_authenticated:
        completed_lesson_ids = set(
            LessonProgress.objects
            .filter(user=request.user, is_completed=True)
            .values_list('lesson_id', flat=True)
        )

    return render(request, 'lessons/list.html', {
        'lessons': lessons,
        'completed_lesson_ids': completed_lesson_ids,
    })


def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    is_completed = False
    if request.user.is_authenticated:
        is_completed = LessonProgress.objects.filter(
            user=request.user, lesson=lesson, is_completed=True
        ).exists()
    return render(request, 'lessons/detail.html', {
        'lesson': lesson,
        'is_completed': is_completed,
    })