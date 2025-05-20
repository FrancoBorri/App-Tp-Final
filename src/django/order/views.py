from rest_framework import viewsets, permissions
from .models import Order, Order_product
from .serializers import OrderSerializer, OrderProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderProductViewSet(viewsets.ModelViewSet):
    serializer_class = OrderProductSerializer
    queryset = Order_product.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
