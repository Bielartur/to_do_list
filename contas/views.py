from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
    return render(request, 'contas/login.html')

def cadastro_usuario(request):
    return render(request, 'contas/cadastro_usuario.html')
