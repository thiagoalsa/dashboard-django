from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', ProductListView.as_view(), name='dashboard'),
    path('products/new/', ProductCreateView.as_view(), name='product-create'),
    path('users/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

]