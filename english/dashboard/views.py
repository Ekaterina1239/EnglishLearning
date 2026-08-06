from django.contrib.auth.decorators import user_passes_test
from django.db.models import Avg, Count
from django.shortcuts import render

from tests_app.models import Test, TestAttempt
from lessons.models import LessonProgress
from users.models import User


def is_moderator(user):
    return user.is_authenticated and (user.is_staff or user.is_moderator)


@user_passes_test(is_moderator, login_url='users:login')
def dashboard_home(request):
    total_users = User.objects.count()
    total_attempts = TestAttempt.objects.count()
    completed_lessons = LessonProgress.objects.filter(is_completed=True).count()

    # Тесты с самым низким средним результатом — сигнал, что вопрос
    # может быть некорректно сформулирован.
    weak_tests = (
        Test.objects
        .annotate(avg_score=Avg('attempts__score_percent'), attempts_count=Count('attempts'))
        .filter(attempts_count__gt=0)
        .order_by('avg_score')[:5]
    )

    context = {
        'total_users': total_users,
        'total_attempts': total_attempts,
        'completed_lessons': completed_lessons,
        'weak_tests': weak_tests,
    }
    return render(request, 'dashboard/home.html', context)