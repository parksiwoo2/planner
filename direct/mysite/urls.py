from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
urlpatterns = [
    path(route="plan/", view=include("plan.urls")),
    path("admin/", admin.site.urls),
    path(route="", view=lambda request: redirect("/plan/")),
]
