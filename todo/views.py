from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import TodoSerializer
from .models import Todo


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all().order_by('priority')
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        # sends user id to the serializer
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}