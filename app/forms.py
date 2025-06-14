from django import forms

class ToDoListForm(forms.Form):
    task = forms.CharField(label='')
