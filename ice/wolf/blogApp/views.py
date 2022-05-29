# from asyncio import tasks
# from multiprocessing import context
# from django.shortcuts import render

# from wolf.blogApp.models import Task

from asyncio import tasks
from django.forms import SlugField
from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    data = Task.objects.all()
    context ={
   'tasks':data
   }
    return render(request, "blogApp/index.html", context)


def detail(request, pk):
    data2 = Task.objects.get(slug=pk)
    context ={
   'tasks':data2}
    return render(request, 'blogApp/detail.html', context)
