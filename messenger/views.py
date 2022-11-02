from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Message
from .forms import ChatMessage
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def contacts(request):
    users = set(User.objects.all())
    users.discard(request.user)
    return render(request, "messenger/contacts.html", {"users" : users})

def messages(request,other_user_str):
    if request.method == "POST":
        formulario = ChatMessage(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            message = data['chat_message']
            sent_by = request.user.username
            received_by = other_user_str
            
            message = Message(message = message,
                              sent_by=sent_by,
                              received_by = received_by)
            message.save()
            return redirect("messages",other_user_str)
        
    else:
        chat_messages = Message.objects.all()
        messages = []
        for message in chat_messages:
            if (request.user.username in message.sent_by and other_user_str in message.received_by) or (other_user_str in message.sent_by and request.user.username in message.received_by):
                messages.append(message)
    formulario = ChatMessage()
    other_user_obj = User.objects.filter(username=other_user_str)
    return render(request, "messenger/messages.html", {"formulario":formulario,"messages":messages,"other_user_str":other_user_str,"other_user_obj":other_user_obj})
