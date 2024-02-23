from django import forms
from .models import ToDoItem

class ToDoForm(forms.ToDoItemForm):
    class Meta:
        model = ToDoItem
        fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
        ]
