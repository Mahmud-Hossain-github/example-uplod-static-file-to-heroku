from django.urls import path
from . import views

urlpatterns = [
    path('',views.dog.as_view(),),
]