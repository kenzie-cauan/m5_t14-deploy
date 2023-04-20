from rest_framework import generics

from parking_lots.permissions import IsAdminOrParkingLotOwner
from .serializers import ParkingLotSerializer
from .models import ParkingLot
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ParkingLotView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ParkingLot.objects.all()

        return ParkingLot.objects.filter(account=self.request.user)

    def perform_create(self, serializer) -> None:
        # from ipdb import set_trace
        # set_trace()

        serializer.save(account=self.request.user)


class ParkingLotDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer
