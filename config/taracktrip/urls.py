
from django.urls import path
from taracktrip.views import Home

urlpatterns = [
    path('', Home.as_view()),
]