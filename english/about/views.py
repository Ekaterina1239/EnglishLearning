from django.shortcuts import render


def methodology(request):
    return render(request, 'about/methodology.html')