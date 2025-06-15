from contas.models import Usuario

def usuario(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(id=request.user.id)
        return {'usuario': usuario}
    else:
        return {'usuario': None}