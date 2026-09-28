from django.shortcuts import render
from django.db.models import Count, Q
from django.core.paginator import Paginator

from .models import Endereco, Estado


def estados(request):


    enderecos = Endereco.objects.all()

    # ==========================================================
    # ESTATÍSTICAS
    # ==========================================================

    total_enderecos = enderecos.count()

    total_estados = (
        enderecos
        .values("uf")
        .distinct()
        .count()
    )

    total_cidades = (
        enderecos
        .values("cidade")
        .distinct()
        .count()
    )

    total_bairros = (
        enderecos
        .values("bairro")
        .distinct()
        .count()
    )

    total_ceps = (
        enderecos
        .values("cep")
        .distinct()
        .count()
    )

    # ==========================================================
    # GRÁFICO DE REGISTROS POR ESTADO
    # ==========================================================

    distribuicao = (
        enderecos
        .values("uf")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    grafico_labels = [
        item["uf"]
        for item in distribuicao
    ]

    grafico_data = [
        item["total"]
        for item in distribuicao
    ]

    # ==========================================================
    # CONTEXTO
    # ==========================================================

    contexto = {

        "total_enderecos": total_enderecos,

        "total_estados": total_estados,

        "total_cidades": total_cidades,

        "total_bairros": total_bairros,

        "total_ceps": total_ceps,

        "grafico_labels": grafico_labels,

        "grafico_data": grafico_data,

        "pagina_atual": "estados",

    }

    return render(
        request,
        "estados.html",
        contexto
    )

def cidades(request):

    uf_filtro = request.GET.get("uf")
    estado_selecionado = None

    if uf_filtro:
        estado_selecionado = (
        Estado.objects
        .filter(uf=uf_filtro)
        .first()
    )
    enderecos = Endereco.objects.all()

    # ==========================================================
    # FILTRO POR ESTADO
    # ==========================================================

    if uf_filtro:
        enderecos = enderecos.filter(uf=uf_filtro)

    # ==========================================================
    # ESTATÍSTICAS
    # ==========================================================

    total_estados = (
        enderecos
        .values("uf")
        .distinct()
        .count()
    )

    total_cidades = (
        enderecos
        .values("cidade")
        .distinct()
        .count()
    )

    total_bairros = (
        enderecos
        .values("bairro")
        .distinct()
        .count()
    )

    total_ceps = (
        enderecos
        .values("cep")
        .distinct()
        .count()
    )

    total_enderecos = enderecos.count()

    # ==========================================================
    # GRÁFICO DE CIDADES
    # ==========================================================

    grafico_labels = []
    grafico_data = []

    if uf_filtro:

        distribuicao = (
            enderecos
            .values("cidade")
            .annotate(total=Count("id"))
            .order_by("-total")
        )

        grafico_labels = [
            item["cidade"]
            for item in distribuicao
        ]

        grafico_data = [
            item["total"]
            for item in distribuicao
        ]

    # ==========================================================
    # ESTADOS DISPONÍVEIS
    # ==========================================================

    estados_disponiveis = (
        Endereco.objects
        .values_list("uf", flat=True)
        .distinct()
        .order_by("uf")
    )

    # ==========================================================
    # CONTEXTO
    # ==========================================================

    contexto = {
        "uf_filtro": uf_filtro,

        "estados_disponiveis": estados_disponiveis,
        "estado_selecionado": estado_selecionado,
        "total_estados": total_estados,
        "total_cidades": total_cidades,
        "total_bairros": total_bairros,
        "total_ceps": total_ceps,
        "total_enderecos": total_enderecos,

        "grafico_labels": grafico_labels,
        "grafico_data": grafico_data,

        "pagina_atual": "cidades",
    }

    return render(
        request,
        "cidades.html",
        contexto
    )  

def bairros(request):

    uf_filtro = request.GET.get("uf")
    cidade_filtro = request.GET.get("cidade")
    bairro_filtro = request.GET.get("bairro")

    enderecos = Endereco.objects.all()

    # Filtro por estado
    if uf_filtro:
        enderecos = enderecos.filter(uf=uf_filtro)

    # Cidades disponíveis
    cidades_disponiveis = []

    if uf_filtro:

        cidades_disponiveis = (
            Endereco.objects.filter(uf=uf_filtro)
            .values_list("cidade", flat=True)
            .distinct()
            .order_by("cidade")
        )

        if cidade_filtro:

            cidade_existe = Endereco.objects.filter(
                uf=uf_filtro, cidade=cidade_filtro
            ).exists()

            if not cidade_existe:
                cidade_filtro = None

    # Bairros disponíveis
    bairros_disponiveis = []

    if uf_filtro and cidade_filtro:

        bairros_disponiveis = (
            Endereco.objects.filter(uf=uf_filtro, cidade=cidade_filtro)
            .exclude(bairro="")
            .values_list("bairro", flat=True)
            .distinct()
            .order_by("bairro")
        )

    # Filtro por cidade
    if cidade_filtro:
        enderecos = enderecos.filter(cidade=cidade_filtro)

    # Filtro por bairro
    if bairro_filtro and cidade_filtro:
        enderecos = enderecos.filter(bairro=bairro_filtro)

    # Cards
    total_estados = enderecos.values("uf").distinct().count()

    total_cidades = enderecos.values("cidade").distinct().count()

    total_bairros = enderecos.values("bairro").distinct().count()

    total_ceps = enderecos.values("cep").distinct().count()

    # Gráfico por bairro
    grafico_labels = []
    grafico_data = []

    if cidade_filtro:

        distribuicao = (
            enderecos.values("bairro").annotate(total=Count("id")).order_by("-total")
        )

        grafico_labels = [
            item["bairro"] if item["bairro"] else "Sem bairro informado"
            for item in distribuicao
        ]

        grafico_data = [item["total"] for item in distribuicao]

    # Paginação
    pagina_obj = None

    if cidade_filtro:

        enderecos_lista = enderecos.order_by("bairro", "logradouro", "cep")

        paginator = Paginator(enderecos_lista, 50)

        numero_pagina = request.GET.get("page")

        pagina_obj = paginator.get_page(numero_pagina)

    # Estados disponíveis
    estados_disponiveis = (
        Endereco.objects.values_list("uf", flat=True).distinct().order_by("uf")
    )

    # Título
    if cidade_filtro:

        grafico_titulo = f"Registros por bairro - {cidade_filtro}"

    else:

        grafico_titulo = "Selecione uma cidade para visualizar os bairros"

    # Contexto
    contexto = {
        "uf_filtro": uf_filtro,
        "cidade_filtro": cidade_filtro,
        "bairro_filtro": bairro_filtro,
        "estados_disponiveis": estados_disponiveis,
        "cidades_disponiveis": cidades_disponiveis,
        "bairros_disponiveis": bairros_disponiveis,
        "total_estados": total_estados,
        "total_cidades": total_cidades,
        "total_bairros": total_bairros,
        "total_ceps": total_ceps,
        "grafico_labels": grafico_labels,
        "grafico_data": grafico_data,
        "grafico_titulo": grafico_titulo,
        "pagina_obj": pagina_obj,
        "pagina_atual": "bairros",
    }

    return render(request, "bairros.html", contexto)

def pesquisa(request):

    termo = request.GET.get("q", "").strip()

    resultados = Endereco.objects.none()

    if termo:

        # Se o usuário digitou exatamente 8 números,
        # tratamos como uma pesquisa direta por CEP.
        if termo.isdigit() and len(termo) == 8:

            resultados = Endereco.objects.filter(cep=termo).order_by(
                "uf", "cidade", "bairro", "logradouro"
            )

        else:

            # Pesquisa global
            resultados = Endereco.objects.filter(
                Q(cep__icontains=termo)
                | Q(logradouro__icontains=termo)
                | Q(bairro__icontains=termo)
                | Q(cidade__icontains=termo)
            ).order_by("uf", "cidade", "bairro", "logradouro", "cep")

    # ==========================================================
    # PAGINAÇÃO
    # ==========================================================

    paginator = Paginator(resultados, 50)

    numero_pagina = request.GET.get("page")

    pagina_obj = paginator.get_page(numero_pagina)

    # ==========================================================
    # CONTEXTO
    # ==========================================================

    contexto = {
        "termo": termo,
        "pagina_obj": pagina_obj,
        "total_resultados": paginator.count,
        "pagina_atual": "pesquisa",
    }

    return render(request, "pesquisa.html", contexto)
