from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    #path('form/', views.fetch_data),
    path('ap/', views.fetch_data),
    path('for/', views.form_data, name="form")
]