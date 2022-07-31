from django.shortcuts import render

tasks = ["bar", "foo", "far"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })