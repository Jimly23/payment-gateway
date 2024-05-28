from django.utils import timezone
from django.db import models

# Create your models here.
class StatusChoice(models.TextChoices):
    PAID = 'PAID', 'Paid'
    UNPAID = 'UNPAID', 'Unpaid'
    PENDING = 'PENDING', 'Pending'
    FAILURE = 'FAILURE', 'Failure'

class Orders(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True, editable=False)
    product = models.CharField(max_length=100, null=True)
    price = models.BigIntegerField()
    qty = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField()
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.UNPAID,)
    order_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self.generate_order_id()
        super().save(*args, **kwargs)

    def generate_order_id(self):
        return f'ord-{str(int(timezone.now().timestamp()))}'

    def __str__(self) -> str:
        return f'{self.order_id} - {self.customer_name} - {self.status}'