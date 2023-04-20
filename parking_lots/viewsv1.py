from rest_framework.views import APIView, Request, Response, status

from .serializers import ParkingLotSerializer
from .models import ParkingLot

from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ParkingLotView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        parking_lots = ParkingLot.objects.all()
        serializer = ParkingLotSerializer(parking_lots, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ParkingLotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(account=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class ParkingLotDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        parking_lot = get_object_or_404(ParkingLot, pk=pk)
        serializer = ParkingLotSerializer(parking_lot)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        parking_lot = get_object_or_404(ParkingLot, pk=pk)
        serializer = ParkingLotSerializer(
            parking_lot, request.data, partial=True
        )
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        parking_lot = get_object_or_404(ParkingLot, pk=pk)
        parking_lot.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
