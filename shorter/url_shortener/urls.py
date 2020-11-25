from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.new, name="new"),
    path("<str:code>", views.code_to_url, name="redirect"),
    path("ranking/<int:limit_ranking>", views.ranking, name="ranking"),
]
