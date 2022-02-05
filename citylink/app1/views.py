from django.shortcuts import render,redirect
from .forms import ZipForm,CityForm
from .models import City,Zip

# Create your views here.


def cityView(request):
    template_name = 'app1/cityview.html'
    form = CityForm()
    context = {'form':form}

    if request.method=='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,template_name,context)


def zipView(request):
    template_name = 'app1/zipview.html'
    form = ZipForm()
    context = {'form':form}

    if request.method=='POST':
        form = ZipForm(request.POST)

        if form.is_valid():
            form.save()




    return render(request,template_name,context)

def citydataView(request):
    template_name = 'app1/citydata.html'
    obj = City.objects.all()
    context = {'data':obj}
    return render(request,template_name,context)



def zipdataView(request):
    template_name = 'app1/zipdata.html'
    data = Zip.objects.all()

    context = {'data':data}

    return render(request,template_name,context)


def updateView(request,id):
    template_name = 'app1/zipview.html'
    obj = Zip.objects.get(area=id)
    form = ZipForm(instance=obj)
    context = {'form':form}

    if request.method=='POST':
        form = ZipForm(request.POST,instance=obj)

        if form.is_valid():
            form.save()

            return redirect('zipdata')


    return render(request,template_name,context)


def deleteView(request,id):
    template_file = 'app1/confirm.html'
    obj = Zip.objects.get(area=id)
    context = {'data':obj}

    if request.method=='POST':
        obj.delete()

        return redirect('zipdata')




    return render(request,template_file,context)



