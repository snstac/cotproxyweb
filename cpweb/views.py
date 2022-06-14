from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins, viewsets, permissions

from .models import COTObject, CPTransform, IconSet, Icon
from .serializers import COTObjectSerializer, CPTransformSerializer, IconSerializer, IconSetSerializer

from django.contrib.auth.models import User, Group


class COTObjectViewSet(viewsets.ModelViewSet):
    queryset = COTObject.objects.all()
    serializer_class = COTObjectSerializer
    lookup_field = 'uid'
#    permission_classes = [permissions.IsAuthenticated]
    lookup_value_regex = '[^/]+'


class COTObjectList(generics.ListCreateAPIView):
    queryset = COTObject.objects.all()
    serializer_class = COTObjectSerializer


class COTObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = COTObject.objects.all()
    serializer_class = COTObjectSerializer


class CPTransformViewSet(viewsets.ModelViewSet): # mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CPTransform.objects.all()
    serializer_class = CPTransformSerializer
    lookup_field = 'cot_uid__uid'
    lookup_value_regex = '[^/]+'


class IconSetViewSet(viewsets.ModelViewSet):
    queryset = IconSet.objects.all()
    serializer_class = IconSetSerializer
    lookup_field = 'uuid'
    lookup_value_regex = '[^/]+'


class IconViewSet(viewsets.ModelViewSet):
    queryset = Icon.objects.all()
    serializer_class = IconSerializer
    lookup_field = 'iconset'
    lookup_value_regex = '[^/]+'