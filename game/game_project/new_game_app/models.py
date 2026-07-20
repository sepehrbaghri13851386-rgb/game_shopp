from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')

    def total_price(self):
        return self.product.gheymat * self.quantity


class game(models.Model):

    GENRE_CHOICES = [
        ('action', 'اکشن'),
        ('adventure', 'ماجراجویی'),
        ('openworld', 'جهان باز'),
        ('sport', 'ورزشی'),
        ('fight', 'مبارزه‌ای'),
        ('horror', 'ترسناک'),
        ('race', 'مسابقه‌ای'),
    ]

    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    title = models.CharField(max_length=100)
    gheymat = models.IntegerField()
    image = models.ImageField(upload_to='game/images/')
    discribshen = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title