from django import forms

class CreatePostForm(forms.Form):
    date = forms.DateTimeField(required=False)
    title = forms.CharField(max_length = 30)
    brief_description = forms.CharField(max_length = 300)
    # category = forms.CharField(max_length = 20)
    # fetured = forms.BooleanField()
    text = forms.CharField(max_length = 300)