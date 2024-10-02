from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name = 'register'),
    path('products/', views.login, name = 'login'),
    path('cart/', views.feedback, name = 'feedback')

]