from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Student Name")
    age = forms.IntegerField(label="Age")
    email = forms.EmailField(label="Email Address")
