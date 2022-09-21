from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from app.models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse('index page')

def hello(request, username):
    return HttpResponse('<h1>hello % s</h1>' % username)

def about(request):
    return HttpResponse('<h1>about me</h1>')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('tasks: %s ' % task.name)