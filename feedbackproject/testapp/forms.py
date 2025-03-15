from django import forms
from django.core import validators
class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    #password = forms.CharField(label='Enter Password',widget=forms.PasswordInput)
    #rpassword = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)

   
    #def clean(self):
        #total_cleaned_data = super().clean()
        #pwd = total_cleaned_data['password']
        #rpwd = total_cleaned_data['rpassword']
        #if pwd != rpwd:
            #raise forms.ValidationError('Both passwords must be same')
    def clean(self):
        total_cleaned_data = super().clean()
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("Request from BOT... Can't be process")