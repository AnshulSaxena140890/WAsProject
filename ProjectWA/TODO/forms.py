from django import forms
from TODO.models import Task

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields=('taskName','taskBrief')
