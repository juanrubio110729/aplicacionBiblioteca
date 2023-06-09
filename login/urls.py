from django.urls import path

from login.views import LoginFormView
from login.views import LogoutView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
