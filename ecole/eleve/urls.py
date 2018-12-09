from django.urls import path
from . import views

urlpatterns = [
    path('inscription',views.inscription_get),
    path('eleve/', views.inscription_post, name=("eleve")),
]
