from django.contrib.auth import logout
from django.http import HttpResponse


def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли из аккаунта')
