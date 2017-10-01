from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic as djangogeneric

from matplotlib import pylab 
from pylab import *
import PIL, PIL.Image
from io import StringIO 

# Create your views here.

from django.http import HttpResponse
from .models import Question,Choice

class IndexView(djangogeneric.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(djangogeneric.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(djangogeneric.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
            
def showimage(request):
    t = arange(0.0,2.0,0.01)
    s = sin(2*pi*t)
    plot(t,s,linewidth=1.0)

    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('This is the test graph')
    grid(True)

    buffer = StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
 
    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), mimetype="image/png")

