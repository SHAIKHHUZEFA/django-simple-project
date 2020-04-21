from django.shortcuts import render,redirect
from .models import Demo
from .import forms

# Create your views here.
def Fin(request):

    dt=Demo.objects.all()
    return render(request,"/Users/Huzefa/PycharmProjects/djangopractice/Testing/templates/test1.html",{'dt':dt})


def Regeister(request):
    form_data=forms.Reg(request.POST or None)

    if form_data.is_valid():
        st=Demo()
        st.first_name = form_data.cleaned_data['first_name']
        st.last_name = form_data.cleaned_data['last_name']
        st.address = form_data.cleaned_data['address']
        st.save()
        return redirect("Fin")
    context={'formreg':form_data}
    return render(request,"/Users/Huzefa/PycharmProjects/djangopractice/Testing/templates/test2.html",context)