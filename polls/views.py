from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


from .models import Choice,Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Retorna as últimas cinco questões publicadas."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Você não selecionou uma escolha.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  

#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  context = {'latest_question_list': latest_question_list}
   # return render(request, 'polls/index.html', context)

#def detalhe(request, question_id):
   # return HttpResponse("Você está olhando para a questão %s." % question_id)

#def detail(request, question_id):
 #  question = get_object_or_404(Question, pk=question_id)
   #return render(request, 
   #'polls/detail.html', {'question': question})
   

#def results(request, question_id):
    #response = "Você está olhando para os resultados da questão %s."
    #return HttpResponse(response % question_id)

#def vote(request, question_id):
   # return HttpResponse("Você está votando na questão %s." % question_id)


#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  template = loader.get_template('polls/index.html')
   # context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))

#def results(request, question_id):
  #  question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/results.html', {'question': question})