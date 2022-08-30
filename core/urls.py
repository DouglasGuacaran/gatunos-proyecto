from django.urls import path
from . views import home, registro, ContactoView, InicioView, Postula, agregapostulacion
from django.contrib.auth import views

urlpatterns = [
    path('',home,name='home'),
    path('postula/',Postula.as_view(),name='postula'),
    path('agregapostulacion/', agregapostulacion),
    path('login/',views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registro/',registro,name='registro'),
    path('inicio/',InicioView.as_view(), name='inicio'),
    path('contacto',ContactoView.as_view(),name='contacto'),
]