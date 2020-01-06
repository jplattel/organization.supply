from rest_framework import serializers

from organization.models import Inventory, Location, Mutation, Product, OrganizationNotification

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "desc"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name", "desc"]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["id", "product", "location", "amount"]


class MutationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mutation
        fields = ["id", "amount", "product", "location", "desc", "operation"]


class GenericNotificationRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Product):
            serializer = ProductSerializer(value)
        if isinstance(value, Location):
            serializer = LocationSerializer(value)
        return serializer.data

class OrganizationNotificationSerializer(serializers.Serializer):
    unread = serializers.BooleanField(read_only=True)
    class Meta:
        model = OrganizationNotification
        fields = [
            "id",
            "timestamp",
            "description",
            "verb",
            "actor_object_content_type",
            "actor_object_id",
            "action_object_content_type",
            "action_object_id"
        ]
