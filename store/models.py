from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name   = models.CharField('Nome do Produto', max_length=200, unique=True)
    slug           = models.SlugField(max_length=200, unique=True)
    description    = models.TextField('Descrição', max_length=500, blank=True)
    price          = models.IntegerField('Preço')
    images         = models.ImageField('Imagem', upload_to='photos/products')
    stock          = models.IntegerField('Estoque')
    is_available   = models.BooleanField('Disponível', default=True)
    category       = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date   = models.DateTimeField('Data de criação', auto_now_add=True)
    modifield_date = models.DateTimeField('Data modificação', auto_now=True)

    class Meta:
        verbose_name        =  'Product'
        verbose_name_plural =  'Products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self) -> str:
        return self.product_name


