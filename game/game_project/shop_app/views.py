from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Shop

def shop(request):
    category = request.GET.get('category')

    if category:
        shops = Shop.objects.filter(category=category)
    else:
        shops = Shop.objects.all()

    paginator = Paginator(shops, 8)  # هر صفحه ۸ محصول
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop_app/shop.html', {
        'shops': page_obj,
        'page_obj': page_obj,
        'category': category,
    })