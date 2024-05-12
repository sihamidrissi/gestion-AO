from django.shortcuts import render

# Header and footer view 

def index(request):
    return render(request,'index.html')