from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models.Pessoa import Pessoa, Departamento
from django.template import loader


def indice(request):
    return HttpResponse("Hello, world. asdasdas")


def pessoa(request, idpessoa):
    p = Pessoa.objects.get(pk=idpessoa)
    dados = {"pessoa": p}
    return render(request, "pessoa/detalhar.html", dados)


def lista_pessoas(request):
    # Aqui é o modelo
    lista_p = Pessoa.objects.obter_pessoas_adultas()
    dados = {"listapessoas": lista_p}

    # Aqui é o template
    template = loader.get_template("pessoa/listar.html")
    return HttpResponse(template.render(dados, request))


def create(request, nome, sobrenome, idade, escolaridade, dpto_descricao):
    novoDepartamento = Departamento(
        sigla=dpto_descricao[0].upper(), descricao=dpto_descricao.upper()
    )
    novoDepartamento.save()
    novaPessoa = Pessoa(
        nome=nome,
        sobrenome=sobrenome,
        idade=idade,
        escolaridade=escolaridade,
        depto_chefia_id=novoDepartamento.id,
    )
    novaPessoa.depto_atual_id = novoDepartamento.id
    novaPessoa.save()

    return JsonResponse(
        {
            "Pessoa criada": [
                {"nome": novaPessoa.nome, "Departamento": dpto_descricao.upper()}
            ]
        }
    )


def update(request, id, dpto_descricao):
    novoDepartamento = Departamento(
        sigla=dpto_descricao[0].upper(), descricao=dpto_descricao.upper()
    )
    novoDepartamento.save()
    pessoa = Pessoa.objects.get(pk=id)
    pessoa.depto_atual_id = novoDepartamento.id
    pessoa.save()
    return JsonResponse(
        {
            "Departamento atualizado": [
                {
                    "nome": pessoa.nome,
                    "novo-departamento": novoDepartamento.descricao.upper(),
                }
            ]
        }
    )


def delete(request, id):
    Pessoa.objects.filter(pk=id).delete()
    return JsonResponse({"Deleted": True})


def testeJson(request):
    payload = {
        "lista": [
            {"nome": "matheus", "sobrenome": "souza"},
            {"nome": "pedro", "sobrenome": "silva"},
        ]
    }

    return JsonResponse(payload)
