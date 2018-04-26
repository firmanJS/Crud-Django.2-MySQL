from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('edit/<int:id>', views.edit),
    path('save', views.save),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
