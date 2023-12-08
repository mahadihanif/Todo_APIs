from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.
class ListTodo(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class DetailTodo(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()    













