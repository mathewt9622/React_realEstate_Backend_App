from django.urls import path,include

from . import views

urlpatterns = [
    path('add/',views.add,name="add"),
    path('view/',views.view,name="view"),
    path('delete/',views.delete,name="delete"),
     path('search/',views.search,name="search"),
]