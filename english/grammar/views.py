from django.shortcuts import get_object_or_404, render
from .models import GrammarTopic


def topic_list(request):
    topics = GrammarTopic.objects.all()
    return render(request, 'grammar/list.html', {'topics': topics})


def topic_detail(request, slug):
    topic = get_object_or_404(GrammarTopic, slug=slug)
    return render(request, 'grammar/detail.html', {'topic': topic})