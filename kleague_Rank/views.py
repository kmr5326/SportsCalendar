from .models import Rank
from .serializers import RankSerializer
from rest_framework import viewsets, response, generics


class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer

rank_list = RankViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

rank_detail = RankViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

