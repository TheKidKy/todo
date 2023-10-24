from rest_framework.viewsets import GenericViewSet
from .serializers import TodoSerializer
from .models import Todo


class TodoViewSet(GenericViewSet):
    queryset = Todo.objects.all().order_by('priority')
    serializer_class = TodoSerializer