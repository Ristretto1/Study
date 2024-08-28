from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from publication_app.forms.login_form import LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {'login_form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('/posts')

        else:
            return redirect('/registration')
