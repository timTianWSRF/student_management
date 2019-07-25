from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from django.urls import reverse


def index(request):
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)


def test(request):
    return render(request, 'test.html', {'document_root': '/student/static'})

# Create your views here.
