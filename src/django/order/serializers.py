from rest_framework import serializers
from .models import Order, Order_product
from product.models import Product


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

    def validate_quantity(self, value):
        """
        Validate quantity is not less than 0
        """
        if value <= 0:
            raise serializers.ValidationError("Quantity must be grater than 0")

    def validate(self, data):
        """
        Validate total price
        """

        product_id = data.get("product_id")  # Obtengo id producto del diccionario data
        quantity = data.get("quantity")  # Obtengo la cantidad de la orden_product
        # Verifico que no esten vacios
        if product_id and quantity:
            try:
                # Traingo instancia de la base de datos del producto con el id
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Invalid product")
            # Precio esperado, precio unitario * la cantidad
            expected_price = product.unit_price * quantity
            if "total_price" in data and data["total_price"] != expected_price:
                raise serializers.ValidationError(
                    f"Total price must be {expected_price}"
                )
            # Asigna el precio correcto y lo guarda en la base de datos
            data["price"] = expected_price
        return data

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
