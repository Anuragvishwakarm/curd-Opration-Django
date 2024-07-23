from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistarion
from .models import user

# Create your views here.

def add_Show(request):
    if request.method == 'POST':
        fm = StudentRegistarion(request.POST)
        if fm.is_valid():
            print("WOLCOM")
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            print("DATA", reg)
            reg.save()
            print("SAVED", reg)
        else:
            print("FORM INVALID")
    else:
        fm = StudentRegistarion()
    stud = user.objects.all()
    return render(request, 'enroll/addShowData.html', {'form': fm,'stu':stud})


def delete(request, id):
    if request.method =='POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update(request, id):
        if request.method== 'POST':
             pi=user.objects.get(pk=id)
             fm = StudentRegistarion(request.POST , instance=pi) 
             if fm.is_valid():
                fm.save()
        else:
             pi=user.objects.get(pk=id)
             fm = StudentRegistarion(instance=pi) 
        return render(request,'enroll/updateData.html' ,{'form':fm})
                      
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
    