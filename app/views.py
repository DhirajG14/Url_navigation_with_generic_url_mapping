from django.shortcuts import render

# Create your views here.
def A(request):
    return render(request,'A.html')

def B(request):
    return render(request,'B.html')