from django import forms

class CreatePostForm(forms.Form):
    # date = forms.DateField()
    # author = forms.CharField(max_length = 30)
    title = forms.CharField(max_length = 30)
    brief_description = forms.CharField(max_length = 300)
    text = forms.CharField(max_length = 300)
    category = forms.CharField(max_length = 20)
    # featured = forms.BooleanField()
    
class SearchPostForm(forms.Form):
    title = forms.CharField(max_length=30,required=False)