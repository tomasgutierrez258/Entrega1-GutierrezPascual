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

def messages(request,other_user):
    
    print("other_user: ",other_user)
    
    if request.method == "POST":
        formulario = ChatMessage(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            message = data['chat_message']
            sent_by = request.user
            received_by = other_user
            
            message = Message(message = message,
                              sent_by=sent_by,
                              received_by = received_by)
            message.save()
            return redirect("messages",other_user)
        
    else:
        chat_messages = Message.objects.all()
        messages = set()
    
        for message in chat_messages:
            if (request.user.username in message.sent_by and other_user in message.received_by) or (other_user in message.sent_by and request.user.username in message.received_by):
                print(message.message)
                messages.add(message)
    
    formulario = ChatMessage()
    return render(request, "messenger/messages.html", {"formulario":formulario,"messages":messages,"other_user":other_user})
