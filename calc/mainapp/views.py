from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import ModelControlActions, Cell_names, Equilibrium
from .serializers import ModelSerializer, CellnameSerializer, EquilibriumSerializer


class ModelViewSet(ModelViewSet):
    queryset = ModelControlActions.objects.all()
    serializer_class = ModelSerializer

class ModelSetView(ViewSet):
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ModelSerializer(queryset, many=True)
        return Response(serializer.data)

    # def list(self, request):
    #     models = ModelControlActions.objects.all()
    #     serializer = ModelSerializer(models, many=True)
    #     return Response(serializer.data)

class Cell_namesViewSet(ModelViewSet):
    queryset = Cell_names.objects.all()
    serializer_class = CellnameSerializer


class EquilibriumViewSet(ModelViewSet):
    queryset = Equilibrium.objects.all()
    serializer_class = EquilibriumSerializer




