from django.urls import path

from .views import HomePageView, cadastroc

from . import views
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('cadastro/', cadastroc),
]
