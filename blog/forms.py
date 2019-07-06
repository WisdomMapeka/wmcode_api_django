from django import forms

class CommentForm(forms.Form):
    your_name = forms.CharField(label='Name', max_length=200)
    message = forms.CharField(widget=forms.Textarea)
