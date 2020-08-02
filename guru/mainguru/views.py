from django.shortcuts import render, redirect
from django.views import View
import telebot
from django.core.mail import send_mail
from .forms import ApplicationsForm


bot = telebot.TeleBot("1225294831:AAHGFJypHdqfCNJZ39zKu3EULzEZvX5hDaU")


def index(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'mainguru/portfolio.html')


def about(request):
    return render(request, 'mainguru/about.html')


def contact(request):
    form = ApplicationsForm()
    return render(request, 'mainguru/contacts.html', {'form': form})


class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Новая заявка!'
            from_email = 'no-reply@bindoors.ru'
            to_email = ['aitofullstackdev@gmail.com', 'aitolivelive@gmail.com']
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя: ' + name + '\r\n' + 'Коммент: ' + comment

            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(-1001412133345, message)
        return redirect('contact')
