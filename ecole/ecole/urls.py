from django.contrib import admin
from django.urls import path,include
from eleve import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acceuil',views.acceuil),
    path('eleve/',include('eleve.urls')),
]
