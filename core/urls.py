from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("leistungen/", views.leistungen, name="leistungen"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("ueber-mich/", views.ueber, name="ueber"),
    path("kontakt/", views.kontakt, name="kontakt"),
    path("kontakt/danke/", views.kontakt_danke, name="kontakt_danke"),
    path("impressum/", views.impressum, name="impressum"),
    path("datenschutz/", views.datenschutz, name="datenschutz"),
]
