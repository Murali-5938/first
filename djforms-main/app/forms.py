from django import forms


class StudentForm(forms.Form):
    stname=forms.CharField(max_length=100)
    stage=forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    password=forms.CharField(widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=[('MALE','Male'),('FEMALE','female')])
    gender=forms.ChoiceField(choices=[('MALE','Male'),('FEMALE','female')],widget=forms.RadioSelect)