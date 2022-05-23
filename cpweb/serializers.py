from rest_framework import serializers
from .models import COTObject, CPTransform


class COTObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COTObject
        fields = ('uid',)


class CPTransformSerializer(serializers.ModelSerializer):
    cot_uid = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=COTObject.objects.all(), required=False)

    class Meta:
        model = CPTransform
        fields = ('callsign', 'cot_uid', 'cot_type', 'icon', 'active')
