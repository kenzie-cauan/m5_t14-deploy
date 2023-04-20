from utils.generic_sets_views import (
    ListCreateGenericView,
    RetrieveUpdateDestroyGenericView,
)

from .serializers import ParkingLotSerializer
from .models import ParkingLot


class ParkingLotView(ListCreateGenericView):
    view_queryset = ParkingLot.objects.all()
    view_serializer = ParkingLotSerializer


class ParkingLotDetailView(RetrieveUpdateDestroyGenericView):
    view_queryset = ParkingLot.objects.all()
    view_serializer = ParkingLotSerializer
