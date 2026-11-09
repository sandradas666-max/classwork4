from django.shortcuts import render
from django.shortcuts import render
def win(request):
    if request.GET:
        username = request.GET.get('username')
        return render(request,'result.html',{
            'formData':request.GET,
            'username': username
        })
    return render(request,'index.html' )

# Create your views here.
