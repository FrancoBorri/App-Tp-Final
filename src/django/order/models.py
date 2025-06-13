from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.status} "

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Order"
        ordering = ["created_at"]


class Order_product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="order_product"
    )
    quantity = models.PositiveBigIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order} - {self.product}"

    class Meta:
        db_table = "order_product"
        verbose_name = "order_product"
        verbose_name_plural = "order_products"
