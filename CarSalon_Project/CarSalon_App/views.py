from django.shortcuts import render

def application_index(request):
    return render(request,'../templates/index.html')