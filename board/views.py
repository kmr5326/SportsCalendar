from .models import Board
from .serializers import BoardSerializer
from rest_framework import viewsets, response, generics


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('-id')
    serializer_class = BoardSerializer


board_list = BoardViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

board_detail = BoardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
