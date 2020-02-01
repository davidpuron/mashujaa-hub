from django.shortcuts import render
from mashujaahub import forms
from telegrambot import sendtelegrammessage
from registration.models import Artisan

# Send Telegram Message to Bot
def sendmessage(request):
    if request.method == 'POST':
        form = forms.SendMessageForm(request.POST)
        if form.is_valid():
            numbers = []
            if form.cleaned_data['number'] != 'None':
                numbers = form.cleaned_data['number'].split(';')

            if form.cleaned_data['group'] != 'NO':
                objs = Artisan.objects.filter(type=form.cleaned_data['group'])
                for artisan in objs:
                    numbers.append(artisan.phone)

            text = form.cleaned_data['text']
            result = ''
            for number in numbers:
                chat_id = sendtelegrammessage.telegram_bot_getchatid(number)
                if (chat_id == -1):
                    result = result +number + ': Error;'
                else:
                    sendtelegrammessage.telegram_bot_sendtext(text,chat_id)
                    result = result + number + ': OK;'
            return render(request,'sendmessageresult.html',{'result': result,'has_permission':True})
            pass  # does nothing, just trigger the validation
    else:
        form = forms.SendMessageForm()
    return render(request, 'sendmessage.html', {'form': form, 'has_permission':True})

# Receive Telegram Message from bot
# Requires previous call https://api.telegram.org/bot<token>/setWebhook?url=https://webapp.mashujaahub.org/receivemessage/
def receivemessage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data["message"]["text"]
        chat_id = message["chat"]["id"]
        print("Received " + message + " message, with Chat ID " + chat_id)
        try:
            Artisan.objects.get(phone=message).update(telegramChatId=chat_id)
            print("Updated " + message + " artisan, with Chat ID " + chat_id)
        except SomeModel.DoesNotExist:
            print(message + " is not one of our artisan phones")

        return JsonResponse({"ok": "POST request processed"})
