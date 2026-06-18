from django.shortcuts import render, get_object_or_404
from .models import Reflection


# Create your views here.


def journal(request):
    reflections = Reflection.objects.filter(
        user=request.user
        ).order_by('-created_on')

    context = {
        'reflections': reflections,
    }
    return render(request, 'journal/journal.html', context)
