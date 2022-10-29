from django import forms

class ChatMessage(forms.Form):
    chat_message = forms.CharField(max_length = 30) 
    
    chat_message.widget.attrs['class']='form-control'