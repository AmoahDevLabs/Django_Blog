from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EdithProfilePageView, CreateProfilePageView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-profile-settings/', UserEditView.as_view(), name='edit-profile-settings'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view()),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('<int:pk>/edit-profile-page', EdithProfilePageView.as_view(), name='edit-profile-page'),
    path('create-profile-page/', CreateProfilePageView.as_view(), name='create-profile-page')
]
