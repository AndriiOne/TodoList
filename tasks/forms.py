from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "tags", "deadline"]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your content...",
                    "rows": 3,
                }
            ),
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                }
            ),
        }

        labels = {
            "content": "What to do",
            "tags": "Tags",
            "deadline": "Deadline",
        }
