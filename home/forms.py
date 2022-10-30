from django import forms
from ckeditor.fields import RichTextFormField

class CreatePostForm(forms.Form):
    # date = forms.DateField()
    # author = forms.CharField(max_length = 30)
    title = forms.CharField(max_length = 60) 
    subtitle = forms.CharField(max_length = 100) 
    brief_description = forms.CharField(max_length = 300)
    text = RichTextFormField(required=False)
    image_post = forms.ImageField(required=False)
    # featured = forms.BooleanField()
    
    title.widget.attrs['class']='form-control'
    subtitle.widget.attrs['class']='form-control'
    brief_description.widget.attrs['class']='form-control'
    text.widget.attrs['class']='form-control'
    
    
class SearchPostForm(forms.Form):
    title = forms.CharField(max_length=60,required=False,label="")
    
    title.widget.attrs['class']='form-control form-control-dark text-bg-dark'
    title.widget.attrs['placeholder']='Search...'
    
