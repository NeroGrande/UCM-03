from django.shortcuts import render

# Create your views here.

def outros(request):
    print('Passei pelo outros')
    return render(request, 'outros/index.html')

def atividade(request):
    print('Passei pelo atividade')
    return render(request, 'outros/atividade.html')

