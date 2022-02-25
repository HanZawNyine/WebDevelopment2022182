from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.utils.text import slugify

# Create your views here.
def home(request):
    task_form = TaskForm()
    tasks = Task.objects.all()
    if request.method == "POST":
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            form = task_form.save(commit=False)
            form.slug = slugify(form.title)
            form.save()
            return redirect("todo:all_tasks")
    return render(request,'todo/home.html',{"tasks":tasks,'task_form':task_form})

def remove(request,year,month,day,slug):
    task = Task.objects.get(created__year=year,created__month=month,created__day=day,slug=slug)
    if request.method == "POST":
        task.delete()
        return redirect("todo:all_tasks")
    return render(request,'todo/delete.html',{"task":task})

def update(request,year,month,day,slug):
    task = Task.objects.get(created__year=year,created__month=month,created__day=day,slug=slug)
    task_form = TaskForm(instance=task)
    if request.method == "POST":
        task_form = TaskForm(instance=task,data=request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("todo:all_tasks")
    return render(request,'todo/update.html',{"task_form":task_form})
    