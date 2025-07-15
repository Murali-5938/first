from django import forms
from app.models import *
class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student 
        fields='__all__'
    reemail=forms.EmailField()
    def clean(self):
        em=self.cleaned_data['stemail']
        reem=self.cleaned_data['reemail']
        if em!=reem:
            raise forms.ValidationError('emails not matched')
        