from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins, viewsets, permissions

from .models import COTObject, CPTransform
from .serializers import COTObjectSerializer, CPTransformSerializer

from django.contrib.auth.models import User, Group


class COTObjectViewSet(viewsets.ModelViewSet):
    queryset = COTObject.objects.all()
    serializer_class = COTObjectSerializer
    lookup_field = 'uid'
#    permission_classes = [permissions.IsAuthenticated]
    lookup_value_regex = '[^/]+'


class CPTransformViewSet(viewsets.ModelViewSet): # mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CPTransform.objects.all()
    serializer_class = CPTransformSerializer
    lookup_field = 'cot_uid__uid'
    lookup_value_regex = '[^/]+'
