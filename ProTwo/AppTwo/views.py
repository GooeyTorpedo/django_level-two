from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
# Create your views here.


# def index(request):
#     return HttpResponse('<em>My Second App</em>')
def index(request):
    return render(request, 'appTwo/index.html')

def user(request):
    user_list = Users.objects.order_by('fname')
    user_dict = {'user': user_list}
    return render(request, 'AppTwo/user.html', context= user_dict)


def help(request):
    my_dict = {'help_insert': 'This is the help page'}
    return render(request, 'AppTwo/help.html', context=my_dict)
