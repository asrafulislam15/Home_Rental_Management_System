from django.shortcuts import render
from .house_models import House
from .form import InsertHouse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def House_info(request):
    Houses = House.objects.all()
    print(Houses)
    context = {
        "Houses": Houses
    }
    return render(request,'House/House_info.html',context)


@login_required
def insertHouseinfo(request):
    form = InsertHouse()
    message="Insert House Information"
    if request.method == 'POST' :
        form = InsertHouse(request.POST)
        message = "Oops,Try again"
        if form.is_valid():
            form.save()
            form = InsertHouse()
            message = "Successfull !"

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'House/inserthouse.html',context)