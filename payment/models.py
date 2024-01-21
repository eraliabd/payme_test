from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    """Order model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.total}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
