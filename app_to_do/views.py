from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        print(task)
    return render(request, 'app_to_do/home.html')
