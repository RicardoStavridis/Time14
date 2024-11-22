from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  

def fale_conosco(request):
    return render(request, 'faleconosco.html')

def doacoes(request):
    return render(request, 'doacoes.html')

def ongs(request):
    return render(request, 'ongs.html')

def orfanatos(request):
    return render(request, 'orfanatos.html') 

def padrinhos(request):
    return render(request, 'padrinhos.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')