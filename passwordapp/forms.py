from django import forms
from .models import PasswordModel

class PasswordForm(forms.ModelForm):

    site_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = PasswordModel
        fields = ('site_url', 'username')


    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['site_url'].widget.attrs.update({'class':'form-control', 'placeholder':'Site URL'})
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'username'})
        self.fields['site_password'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})