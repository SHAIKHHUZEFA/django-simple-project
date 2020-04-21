from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("Register", views.Regeister,name="Register"),
    path("/",views.Fin,name="Fin")
]
