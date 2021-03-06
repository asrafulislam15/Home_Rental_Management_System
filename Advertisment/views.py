from django.shortcuts import render
from .advertisment_models import Advertisement
from .form import Insertadvertisment
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def advertisementinfo(request):
    advertisment = Advertisement.objects.all()
    print(advertisment)
    context = {
        "Advertisment": advertisment
    }
    return render(request,'advertisement/advertisement_info.html',context)


@login_required
def insertadvertismentinfo(request):
    form = Insertadvertisment()
    message="Insert House Information"
    if request.method == 'POST' :
        form = Insertadvertisment(request.POST)
        message = "Oops,Try again"
        if form.is_valid():
            form.save()
            form = Insertadvertisment()
            message = "Successfull !"

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'advertisement/insertadvertisment.html',context)

