from django.urls import path
from .views import Register, UserEditeView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('edit_profile/', UserEditeView.as_view(), name='edit_profile')
]
