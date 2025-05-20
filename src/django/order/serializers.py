from rest_framework import serializers
from .models import Order, Order_product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["id", "user", "created_at"]
        extra_kwargs = {
            "status": {"required": True},
        }

    def create(self, validated_data):
        """
        Create a new order with the provided validated data.
        """
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update order with the provided validated data.
        """
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_product
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {"quantity": {"required": True}, "price": {"required": True}}

    def create(self, validated_data):
        """
        Create a new order_pruduct with the provided validated data.
        """
        return Order_product.objects.create(**validated_data)

    def update(self, instance, valdiated_data):
        """
        Update order_product with the provided validated data.
        """
        instance.quantity = valdiated_data.get("quantity", instance.status)
        instance.price = valdiated_data.get("price", instance.price)
        instance.save()
        return instance
