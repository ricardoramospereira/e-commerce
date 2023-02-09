from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id    = models.CharField("Id Carrinho", max_length=250, blank=True)
    date_added = models.DateField("Data de registro", auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey("Produto", Product, on_delete=models.CASCADE)
    cart    = models.ForeignKey("Carrinho", Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantidade")
    is_active = models.BooleanField("Ativo", default=True)

    def __str__(self) -> str:
        return self.product
