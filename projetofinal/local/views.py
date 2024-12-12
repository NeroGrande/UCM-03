from django.shortcuts import render
# Create your views here.

def local(request):
    print('Passei pelo local')
    return render(request, 'local/index.html')

def ondeestamos(request):
    print('Passei pelo ondeestamos')
    return render(request, 'local/ondeestamos.html')

