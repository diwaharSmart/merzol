
from django.urls import path,include
from Account import views


urlpatterns = [
    path('check-user/',    views.UserView.as_view()),
    path('register-user/', views.UserView.as_view()),
]
