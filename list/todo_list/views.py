from rest_framework import viewsets, filters, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import  TaskSerializer
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['competed']
    search_fields = ['title']
    ordering_fields = ['created_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
