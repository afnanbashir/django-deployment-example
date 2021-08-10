from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
]
