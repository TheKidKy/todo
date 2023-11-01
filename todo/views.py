from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer
from .models import Todo


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all().order_by('priority')
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        # sends user id to the serializer
        serializer.save(user=self.request.user)