from django import forms
from .models import Post



class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #fields = ['name', 'cover', 'email', 'phno', 'adrss1', 'adrss2']
        fields = ['title', 'cover', 'email', 'phno', 'adrss1', 'adrss2', 'dob']

        widgets = {
            'publish_date': DateInput(),
         }