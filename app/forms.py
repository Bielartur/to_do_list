from django import forms

class ToDoForm(forms.Form):
    task = forms.CharField(label='')
