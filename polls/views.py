from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse('Olá mundo! Essa é uma resposta HTTP.')

def detalhe(request, question_id):
    return HttpResponse("Você está olhando para a questão %s." % question_id)

def resultados(request, question_id):
    response = "Você está olhando para os resultados da questão %s."
    return HttpResponse(response % question_id)

def voto(request, question_id):
    return HttpResponse("Você está votando na questão %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)