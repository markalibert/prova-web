from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.estados,
        name="inicio"
    ),

    path(
        "estados/",
        views.estados,
        name="estados"
    ),

    path(
        "cidades/",
        views.cidades,
        name="cidades"
    ),

    path(
        "bairros/",
        views.bairros,
        name="bairros"
    ),

    path(
        "pesquisa/",
        views.pesquisa,
        name="pesquisa"
    ),

]