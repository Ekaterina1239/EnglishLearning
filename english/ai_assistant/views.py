from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .services import build_feedback


@login_required
def explain_last_mistakes(request):
    wrong_answers = request.session.get('last_wrong_answers', [])

    if not wrong_answers:
        return render(request, 'ai_assistant/explanation.html', {'no_mistakes': True})

    feedback = build_feedback(wrong_answers)
    return render(request, 'ai_assistant/explanation.html', {'feedback': feedback})