from unicodedata import name
from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.showEntry_url, name="show_entry"),
    path("search", views.search, name="search"),
    path("create_edit", views.create_edit, name="create_edit"),
    path("wiki/<str:name>/edit",views.edit, name="edit"),
    path("random", views.random, name="random"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
