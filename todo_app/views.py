from django.views.generic import ListView

from .models import TodoList


class ListView(ListView):
    model = TodoList
    template_name = "todo_app/index.html"
