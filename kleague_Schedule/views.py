from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework import viewsets, response, generics


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


schedule_list = ScheduleViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

schedule_detail = ScheduleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
