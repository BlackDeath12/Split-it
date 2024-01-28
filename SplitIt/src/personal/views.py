from django.shortcuts import render
from personal.models import Question
from account.models import Account

# Create your views here.
def home_screen_view(request):
    context = {}
    context['some_string'] = "this is some string that im passing for the view"

    questions = Question.objects.all()
    context['questions'] = questions

    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "personal/home.html", context)

def payment_screen_view(request):

    context = {}
    return render(request, "personal/payment.html", context)