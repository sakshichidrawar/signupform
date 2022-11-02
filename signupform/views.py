from django.shortcuts import render
from signupform.forms import signform

# Create your views here.
def signupview(request):
    form=signform()
    if request.method =='POST':
        form=signform(request.POST)
        if form.is_valid():
            print('form validated')
            print('Password:',form.cleaned_data['password'])
            print('rpassword:',form.cleaned_data['rpassword'])
    return render(request,'signupform/input.html',{'form':form})

