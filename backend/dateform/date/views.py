from rest_framework.generics import CreateAPIView
from .models import Year
from .serializers import YearCreateSerializer


class CreateYear(CreateAPIView):
    queryset = Year.objects.all()
    serializer_class = YearCreateSerializer
