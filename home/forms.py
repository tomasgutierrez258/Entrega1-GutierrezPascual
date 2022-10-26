from django import forms

class CreatePostForm(forms.Form):
    # date = forms.DateField()
    # author = forms.CharField(max_length = 30)
    title = forms.CharField(max_length = 30) 
    brief_description = forms.CharField(max_length = 300)
    text = forms.CharField(max_length = 300)
    image_post = forms.ImageField(required=False)
    # featured = forms.BooleanField()
    
    title.widget.attrs['class']='form-control'
    brief_description.widget.attrs['class']='form-control'
    text.widget.attrs['class']='form-control'
    
    
class SearchPostForm(forms.Form):
    title = forms.CharField(max_length=30,required=False,label="")
    
    title.widget.attrs['class']='form-control form-control-dark text-bg-dark'
    title.widget.attrs['placeholder']='Search...'