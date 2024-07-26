from django.urls import path
from . import views

urlpatterns = [
    path("<str:type>", views.Type.as_view(), name="Type"),
]
