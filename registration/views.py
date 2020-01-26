from django.shortcuts import render
from mashujaahub import forms
from telegrambot import sendtelegrammessage

# Create your views here.
def sendmessage(request):
    if request.method == 'POST':
        form = forms.SendMessageForm(request.POST)
        if form.is_valid():
            numbers = form.cleaned_data['number'].split(';')
            text = form.cleaned_data['text']
            result = ''
            for number in numbers:
                chat_id = sendtelegrammessage.telegram_bot_getchatid(number)
                if (chat_id == -1):
                    result = result +number + ': Error;'
                else:
                    sendtelegrammessage.telegram_bot_sendtext(text,chat_id)
                    result = result + number + ': OK;'
            return render(request,'sendmessageresult.html',{'result': result})
            pass  # does nothing, just trigger the validation
    else:
        form = forms.SendMessageForm()
    return render(request, 'sendmessage.html', {'form': form})
