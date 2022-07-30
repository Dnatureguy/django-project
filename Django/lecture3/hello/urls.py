from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bammy", views.bammy, name="bammy"),
    path("david", views.david, name="david")
]
