from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceLoginView.as_view(), name='login'),
    path('logout/', views.LoginInterfaceLogoutView.as_view(), name='logout'),
]