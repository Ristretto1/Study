from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from publication_app.forms.profile_form import ProfileForm


class ProfileView(View):
    def get(self, request):
        if request.user.id:
            user = User.objects.get(id=request.user.id)
            form = ProfileForm()

            context = {'user': user, 'profile_form': form}
            return render(request, 'profile.html', context)
        return redirect('/login')

    def post(self, request):
        # User.objects.filter(id=request.user.id).update(first_name=request.POST['first_name'],
        #                                                last_name=request.POST['last_name'])
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save(update_fields=['first_name', 'last_name'])

        return redirect('/profile')
