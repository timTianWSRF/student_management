from django.shortcuts import render
from .models import Student
import os
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from homework.models import Homework
from django.urls import reverse


def index(request):
    homeworks = Homework.get_all()
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'homeworks': homeworks,
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)


def test(request):
    return render(request, 'test.html', {'document_root': '/student/static'})


def test2(request):
    return render(request, 'test2.html')


def upload_file(request):
    homeworks = Homework.get_all()
    students = Student.get_all()

    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:\\", myFile.name), 'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = StudentForm()

        context = {
            'homeworks': homeworks,
            'students': students,
            'form': form,
        }
        return render(request, 'index.html', context=context)
# Create your views here.
