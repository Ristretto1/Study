from django.shortcuts import render, redirect
from django.views import View

from publication_app.forms.registration_form import RegistrationForm


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'reg_form': form}
        return render(request, 'registration.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts')
