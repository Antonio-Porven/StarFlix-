from django.urls import path, include
#imports views.py into urls.py
from . import views
urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signup/', views.signup_view, name='signup'),

]
