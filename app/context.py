from contas.models import Usuario

def usuario(request):
    usuario = Usuario.objects.get(id=request.user.id)
    return {'usuario': usuario}