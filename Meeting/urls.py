
from django.urls import path,include
from Meeting import views


urlpatterns = [
    path('get-meeting/',    views.MeetingtView.as_view()),
]
