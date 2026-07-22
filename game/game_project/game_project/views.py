from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from new_game_app.models import game, CartItem
from shop_app.models import Shop
from coment_app.forms import ComentForm


def home(request):
    games = game.objects.all()
    return render(request, 'index.html', {'games': games})


def search(request):
    query = request.GET.get('q', '').strip()
    game_results = []
    shop_results = []
    if query:
        game_results = game.objects.filter(title__icontains=query)
        shop_results = Shop.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {
        'query': query,
        'game_results': game_results,
        'shop_results': shop_results,
    })


def product_detail(request, id):
    product = get_object_or_404(game, id=id)
    
    related_games = game.objects.filter(genre=product.genre).exclude(id=id)[:4]
    
    related_shops = Shop.objects.filter(category=product.genre)[:4]
    
    return render(request, 'product-details.html', {
        'product': product,
        'related_games': related_games,
        'related_shops': related_shops,
    })

def contact(request):
    if request.method == 'POST':
        form = ComentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ComentForm()
    return render(request, 'contact.html', {'form': form})


@login_required(login_url='/login/')
def sabad(request):
    cart_items = CartItem.objects.filter(user=request.user)

    cart_total_qty = sum(item.quantity for item in cart_items)
    cart_subtotal = sum(item.total_price() for item in cart_items)

    shipping_cost = 0 if cart_subtotal >= 500000 else 50000
    cart_total = cart_subtotal + shipping_cost

    cart_items_list = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'total_price': item.total_price(),
        }
        for item in cart_items
    ]

    return render(request, "sabad.html", {
        "cart_items": cart_items_list,
        "cart_total_qty": cart_total_qty,
        "cart_subtotal": cart_subtotal,
        "shipping_cost": shipping_cost,
        "cart_total": cart_total,
    })


@login_required(login_url='/login/')
def add_to_cart(request, id):
    product = get_object_or_404(game, id=id)
    ct = ContentType.objects.get_for_model(game)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=ct,
        object_id=product.id,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("sabad")


@login_required(login_url='/login/')
def add_shop_to_cart(request, id):
    product = get_object_or_404(Shop, id=id)
    ct = ContentType.objects.get_for_model(Shop)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=ct,
        object_id=product.id,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("sabad")


@login_required(login_url='/login/')
def cart_remove(request, id):
    CartItem.objects.filter(user=request.user, object_id=id).delete()
    return redirect("sabad")


@login_required(login_url='/login/')
def cart_increase(request, id):
    item = CartItem.objects.filter(user=request.user, object_id=id).first()
    if item:
        item.quantity += 1
        item.save()
    return redirect("sabad")


@login_required(login_url='/login/')
def cart_decrease(request, id):
    item = CartItem.objects.filter(user=request.user, object_id=id).first()
    if item:
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
    return redirect("sabad")


def checkout(request):
    return render(request, "pardakht.html", {})