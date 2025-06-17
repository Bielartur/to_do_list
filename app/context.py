from contas.models import Usuario
from app.models import ToDoList

def qtd_concluidas(request):
    if request.user.is_authenticated:
        concluidas = ToDoList.objects.filter(user_id=request.user.id, done=True).count()
        total = ToDoList.objects.filter(user_id=request.user.id).count()
        return {'concluidas': concluidas, 'total': total}
    else:
        return {'concluidas': None, 'total': None}