from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import generics, mixins, viewsets, permissions

from .models import COTObject, CPTransform, IconSet, Icon, Queue, Route
from .serializers import (
    COTObjectSerializer,
    CPTransformSerializer,
    IconSerializer,
    IconSetSerializer,
    QueueSerializer,
    RouteSerializer,
)

from django.contrib.auth.models import User, Group


class COTObjectViewSet(viewsets.ModelViewSet):
    queryset = COTObject.objects.all()
    serializer_class = COTObjectSerializer
    lookup_field = "uid"
    #    permission_classes = [permissions.IsAuthenticated]
    lookup_value_regex = "[^/]+"


class COTObjectList(generics.ListCreateAPIView):
    queryset = COTObject.objects.all()
    serializer_class = COTObjectSerializer


class COTObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = COTObject.objects.all()
    serializer_class = COTObjectSerializer
    lookup_field = "uid"
    lookup_value_regex = "[^/]+"


class CPTransformList(generics.ListCreateAPIView):
    queryset = CPTransform.objects.all()
    serializer_class = CPTransformSerializer
    lookup_field = "cot_uid"
    lookup_value_regex = "[^/]+"


class CPTransformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPTransform.objects.all()
    serializer_class = CPTransformSerializer
    lookup_field = "cot_uid"
    lookup_value_regex = "[^/]+"


class IconSetList(generics.ListCreateAPIView):
    queryset = IconSet.objects.all()
    serializer_class = IconSetSerializer
    lookup_field = "uuid"
    lookup_value_regex = "[^/]+"


class QueueList(generics.ListCreateAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer
    lookup_field = "queue"
    lookup_value_regex = "[^/]+"


class QueueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer
    lookup_field = "queue"
    lookup_value_regex = "[^/]+"


class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    lookup_field = "source"
    lookup_value_regex = "[^/]+"


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RouteSerializer
    lookup_field = "source__queue"
    lookup_value_regex = "[^/]+"
    lookup_url_kwarg = "source"

    def get_queryset(self):
        queryset = Route.objects.filter(source__queue=self.kwargs["source"])
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.first()
        if obj is None:
            raise Http404("No Route matches the given query.")
        return obj


class IconSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IconSet.objects.all()
    serializer_class = IconSetSerializer
    lookup_field = "uuid"
    lookup_value_regex = "[^/]+"


class IconList(generics.ListCreateAPIView):
    queryset = Icon.objects.all()
    serializer_class = IconSerializer
    lookup_field = "name"
    lookup_value_regex = "[^/]+"


class IconDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Icon.objects.all()
    serializer_class = IconSerializer
    lookup_field = "name"
    lookup_value_regex = "[^/]+"


##### OLD
class CPTransformViewSet(
    viewsets.ModelViewSet
):  # mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CPTransform.objects.all()
    serializer_class = CPTransformSerializer
    # lookup_field = 'cot_uid__uid'
    lookup_value_regex = "[^/]+"


class IconSetViewSet(viewsets.ModelViewSet):
    queryset = IconSet.objects.all()
    serializer_class = IconSetSerializer
    lookup_field = "uuid"
    lookup_value_regex = "[^/]+"


class IconViewSet(viewsets.ModelViewSet):
    queryset = Icon.objects.all()
    serializer_class = IconSerializer
    lookup_field = "iconset"
    lookup_value_regex = "[^/]+"
