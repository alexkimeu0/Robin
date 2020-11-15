from django.shortcuts import render


def index(request):
    user = request.user
    return render(request, 'main/index.html', {'user': user})
