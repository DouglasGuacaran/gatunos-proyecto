from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import CustomerUserCreation,ContactoForm
from django.views.generic import View
from . models import Gatos,Postulacion
from django.contrib import messages
# Create your views here.

def home(request):
    
    return render(request,'home.html')

def login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request, f'{username} Bienvenido a tu cuenta!')
                return redirect('/')    
            else:
                messages.warning(request, 'Lo sentimos, datos de cuenta inválidos!')
                return HttpResponse("<h1> Cuenta no activa</h1>")
        else:
            messages.warning(request, 'Clave de usuario o cuenta inválida!')
            HttpResponse("<h1>Clave de usuario o cuenta inválida</h1>")
    return render(request,'registration/login.html',{'page':page})

def registro(request):
    data={
        'form':CustomerUserCreation()
    }
    
    if request.method == 'POST':
        form = CustomerUserCreation(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada satisfactoriamente!, {username} ')
            return redirect('/accounts/login')
    return render(request,'registro.html', data)

class ContactoView(View):
    def get(self, request, *args, **kwargs):
        form = ContactoForm()
        context={
            'form': form,
        }
        return render(request,'contacto.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactoForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('/contacto')
            
class InicioView(View):
    def get(self, request, *args, **kwargs):

        context={

        }
        return render(request,'inicio.html', context)

class Postula(View):
    def get(self, request, *args, **kwargs):
        gatos= Gatos.objects.all()
        context={
            'gatos': gatos
        }
        return render(request,'postula.html', context)

def agregapostulacion(request):
    
    email= request.POST.get('email')
    rut = request.POST.get('rut')
    username = request.POST.get('username')
    fecha_nac = request.POST.get('fecha_nac')
    telefono = request.POST.get('telefono')
    regiones = request.POST.get('regiones')
    comunas = request.POST.get('comunas')
    direccion= request.POST.get('direccion')
    tipo_vivienda = request.POST.get('tipo_vivienda')
    gato_name=request.POST.get('gato_name')
    gato = Gatos.objects.get(gato_name=gato_name)
    
    postulacion = Postulacion.objects.create(email=email, rut=rut, username=username,fecha_nac=fecha_nac,telefono=telefono,regiones=regiones,comunas=comunas, direccion=direccion,tipo_vivienda=tipo_vivienda,gato=gato)
    messages.success(request, f'Gracias por postular {username}')
    return redirect('/inicio')
