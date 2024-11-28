from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("freecash/", include("freecash.urls")),
    path("admin/", admin.site.urls),
]