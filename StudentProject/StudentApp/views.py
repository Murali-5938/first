from django.shortcuts import render
from .forms import StudentForm

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return render(request, 'success.html', {'name': name})
    else:
        form = StudentForm()

    return render(request, 'student_registration.html', {'form': form})
