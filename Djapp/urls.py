from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add_book/', views.add_book, name='add_book'),
    path('signin/', views.login_user, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout', views.logout_user, name='logout')

]
