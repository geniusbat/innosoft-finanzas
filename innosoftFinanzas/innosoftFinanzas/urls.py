"""innosoftFinanzas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views
from usuarios import views as usuariosViews
from administrador import views as adminViews
from inventario import views as inventarioViews
from necesidades import views as necesidadesViews

#Comentar en mayusculas el módulo al que se refiere la url

urlpatterns = [
    path('',views.index),
    path('superadmin/', admin.site.urls),
    #USUARIOS
    #Login
    path('login/', usuariosViews.login, name="login"),
    path('handlelogin/', usuariosViews.handleLogin, name="handleLogin"),
    path('loginerror/', usuariosViews.loginError),
    path('loginsucces/', usuariosViews.loginSuccesful),
    #Register
    path('register/', usuariosViews.register, name="register"),
    path('handleregistration/', usuariosViews.handleRegistration, name="handleRegistration"),
    #ADMINISTRADOR
    path("admin/", adminViews.index, name="adminIndex"),
    path("admin/usuarios", adminViews.usuarios, name="adminUsuarios"),
    path("admin/usuarios/nuevo", adminViews.nuevoUsuario, name="nuevoUsuario"),
    path("admin/usuarios/handlenuevo", adminViews.handleNuevoUsuario, name="handleNuevoUsuario"),
    path("admin/usuarios/modificar/<str:uvus>", adminViews.modificarUsuario),
    path("admin/usuarios/handle", adminViews.handleModificarUsuario, name="handleModificarUsuario"),
    path("admin/usuarios/eliminar/<str:uvus>", adminViews.eliminarUsuario),
    #INVENTARIO
    path("inventario/nuevoProducto", inventarioViews.formProducto, name="nuevoProducto"),
    path("inventario/modificarProducto/<str:id>", inventarioViews.modificarProducto, name="modificarProducto"),
    path("inventario/handleModificarProducto", inventarioViews.handlemodificarProducto, name="handleModificarProducto"),
    path("inventario/productos", inventarioViews.listProducto, name="productos"),
    path("inventario/productos/eliminar/<str:id>", inventarioViews.eliminarProducto),
    path("inventario/nuevaCategoria", inventarioViews.formCategoria, name="nuevoCategoria"),
    path("inventario/categoria/eliminar/<str:id>", inventarioViews.eliminarCategoria),
    #NECESIDADES
    path("necesidades/handleModificarNecesidad", necesidadesViews.handlemodificarNecesidad, name="handleModificarNecesidad"),
    path("necesidades/modificar/<str:id>", necesidadesViews.modificarNecesidad, name="modificarNecesidad"),
    path("necesidades/necesidades", necesidadesViews.listNecesidad, name="necesidades"),
    path("necesidades/nuevaNecesidad", necesidadesViews.formNecesidad, name="nuevaNecesidad"),
    path("necesidades/eliminar/<str:id>", necesidadesViews.eliminarNecesidad),
    path("necesidades/nuevoComite", necesidadesViews.formComite, name="nuevoComite"),
    path("necesidades/comite/eliminar/<str:id>", necesidadesViews.eliminarComite),
]
