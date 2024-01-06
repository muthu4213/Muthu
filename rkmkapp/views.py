from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
# Create your views here.

# def retrive_view(request):
#     student = Student.objects.all()
#     return render(request, 'rkmkapp/index.html',context={'student':student})

def create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create')
    return render(request, 'rkmkapp/index.html',context={'form':form})
