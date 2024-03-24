from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    context = {
        'tasks': tasks,
        'form': form,
    }

    return render(request, 'tasks/home.html', context)


def update_status(request,pk):
    task = Task.objects.get(pk=pk)

    if task.status == 'ToDo':
        task.status = 'InProgress'
    elif task.status == 'InProgress':
        task.status = 'Completed'
    task.save()

    return redirect('home')