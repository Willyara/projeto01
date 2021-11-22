from django.http import HttpResponse


def index(request):
    return HttpResponse('Olá mundo! Essa é uma resposta HTTP.')

def detalhe(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def resultados(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def voto(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)