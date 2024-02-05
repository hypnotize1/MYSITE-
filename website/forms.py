from django import forms
from website.models import Contact, newsletter 

class name_form(forms.Form):
    name = forms.CharField(max_length = 255)
    email = forms.EmailField()
    subject = forms.CharField(max_length = 255)
    message = forms.CharField(widget = forms.Textarea)
    


class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



class newsletter_form(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'
















        