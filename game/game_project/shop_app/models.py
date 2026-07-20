from django.db import models


class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'اکشن'),
        ('adventure', 'ماجراجویی'),
        ('openworld', 'جهان باز'),
        ('sport', 'ورزشی'),
        ('fight', 'مبارزه‌ای'),
        ('horror', 'ترسناک'),
        ('race', 'مسابقه‌ای'),
    ]

    title = models.CharField(max_length=50, verbose_name='عنوان')
    image = models.ImageField(upload_to='shop/images', verbose_name='تصویر')
    gheymat = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='قیمت')
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='action',
        verbose_name='سبک'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'