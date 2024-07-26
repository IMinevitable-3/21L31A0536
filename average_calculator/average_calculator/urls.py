from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("numbers/", include(("calci.urls", "calci"), namespace="calci")),
]
