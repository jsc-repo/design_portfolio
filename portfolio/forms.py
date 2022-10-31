from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100, required=True)
    surname = name = forms.CharField(max_length = 100, required=True)
    from_email = forms.EmailField(required=True)
    msg = forms.CharField(widget=forms.Textarea)
