from django.shortcuts import render, get_object_or_404, redirect
from .models import Reflection
from .forms import ReflectionForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def journal(request):
    reflections = Reflection.objects.filter(
        user=request.user
        ).order_by('-created_on')

    context = {
        'reflections': reflections,
    }
    return render(request, 'journal/journal.html', context)


@login_required
def add_reflection(request):

    if request.method == 'POST':
        form = ReflectionForm(request.POST)
        if form.is_valid():
            reflection = form.save(commit=False)
            reflection.user = request.user
            reflection.save()

            return redirect('journal')

    else:
        form = ReflectionForm()

    context = {
            'form': form
        }
    return render(request, 'journal/add_reflection.html', context)
