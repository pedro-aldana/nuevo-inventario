from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.HomeView, name="home"),
    
    path('', include('inventory.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='salir.html'), name="logout"),
]
