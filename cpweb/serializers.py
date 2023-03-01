from rest_framework import serializers
from .models import COTObject, CPTransform, Icon, IconSet, Queue, Route


class COTObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COTObject
        fields = ("uid", "n_number")


class CPTransformSerializer(serializers.ModelSerializer):
    cot_uid = serializers.PrimaryKeyRelatedField(
        allow_null=True, queryset=COTObject.objects.all(), required=False
    )

    class Meta:
        model = CPTransform
        fields = (
            "callsign",
            "cot_uid",
            "cot_type",
            "icon",
            "active",
            "domain",
            "agency",
            "reg",
            "model",
            "hex",
        )


class IconSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IconSet
        fields = ("uuid", "name")


class QueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Queue
        fields = ["queue"]


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    source = serializers.SerializerMethodField()
    destination = serializers.SerializerMethodField()

    def get_source(self, obj):
        return obj.source.queue if obj.source else None

    def get_destination(self, obj):
        return obj.destination.queue if obj.destination else None

    class Meta:
        model = Route
        fields = ("name", "source", "destination")


class IconSerializer(serializers.HyperlinkedModelSerializer):
    iconset = serializers.PrimaryKeyRelatedField(
        allow_null=True, queryset=IconSet.objects.all(), required=False
    )

    class Meta:
        model = Icon
        fields = ("name", "iconset")
