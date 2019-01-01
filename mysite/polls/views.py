from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect   # import HttpResponseRedirect
from .models import Question, Choice 
from django.urls import reverse


def index(request):
	latest_question_list = Question.objects.all()
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)  # using get_object_or_404
	template = 'polls/detail.html'
	context = {'question': question}
	return render(request, template, context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print('Choice')
    print(request.POST['choice'])
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))