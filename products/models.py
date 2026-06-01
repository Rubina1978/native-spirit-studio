from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    available_sizes = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.name

    def has_size_variants(self):
        size_categories = {'blankets', 'rugs'}
        return bool(
            self.category
            and self.category.name in size_categories
            and self.sizes.exists()
        )

    # assistance of github copilot

    def get_lowest_size_price(self):
        lowest_size = self.sizes.order_by('price').first()
        return lowest_size.price if lowest_size else self.price


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='sizes',
        on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} - {self.label}'

    class Meta:
        verbose_name = 'Product Size'
        verbose_name_plural = 'Product Sizes'
