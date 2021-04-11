from django.urls import path
from .views import Register, UserEditeView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('edit_profile/', UserEditeView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_pass.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_pass.html')),
    path('password_succss/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile_page/', CreateProfilePage.as_view(), name="create_profile_page"),
]
