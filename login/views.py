from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'login/index.html')


def submit(request):
    try:
        username, password = request.POST['pollingUsername'], request.POST['pollingPassword']
        if len(username) == 0 or len(password) == 0:
            raise Exception('Username and password are required.')
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise Exception('Incorrect username or password.')
    except Exception as e:
        return render(request, 'login/index.html', {
            'error_message': e.args[0],
        })
    else:
        login(request, user)
        return HttpResponseRedirect('/polls')
