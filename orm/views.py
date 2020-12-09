from django.shortcuts import render
from .forms import UserName
from .models import *
def index(request):
    form = UserName()

    if request.method == 'POST':
        form = UserName(request.POST)
        if form.is_valid():
            form.save()
    objs = User.objects.all()
    context = {'form':form, 'objs':objs}
    return render(request, 'index.html', context)

def new_index(request):
    objs = User.objects.all()
    context = {'objs':objs}
    return render(request,'other.html', context)