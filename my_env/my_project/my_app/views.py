from django.shortcuts import render, get_object_or_404
from .models import Candidatedirectory



# Create your views here.

def candidate_list(request):
    candidates = Candidatedirectory.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    return render(request, 'candidate_detail.html', {'candidate': candidate})

def candidate_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass  # Placeholder for handling form submission
    else:
        # Render empty form
        return render(request, 'candidate_form.html')


def candidate_update(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass  # Placeholder for handling form submission
    else:
        # Render form with instance data
        return render(request, 'candidate_form.html')


def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    if request.method == 'POST':
        # Handle deletion
        return render(request, 'candidate_confirm_delete.html', {'candidate': candidate})
