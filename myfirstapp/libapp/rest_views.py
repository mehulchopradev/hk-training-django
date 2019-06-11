from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PublicationHouseSerializer
from .models import PublicationHouse

class PublicationList(ListCreateAPIView):
    queryset = PublicationHouse.objects.all()
    serializer_class = PublicationHouseSerializer

class GetPublication(RetrieveUpdateDestroyAPIView):
    queryset = PublicationHouse.objects.all()
    serializer_class = PublicationHouseSerializer