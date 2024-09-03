from django.urls import path, include

from publication_app.api.views.router import api_router
from publication_app.views.login import LoginView
from publication_app.views.logout import LogoutView
from publication_app.views.posts import PostsView
from publication_app.views.profile import ProfileView
from publication_app.views.registration import RegistrationView

urlpatterns = [
    path('posts/', PostsView.as_view(), name='main_page'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('api/', include(api_router.urls)),
]
