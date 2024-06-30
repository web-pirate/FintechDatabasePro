from django.urls import path
from user_auths import views

app_name = "user_auths"

urlpatterns = [
    path("sign-up/", views.RegisterView, name="sign-up")
]
