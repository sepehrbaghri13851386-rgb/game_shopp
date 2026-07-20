from django.shortcuts import render,get_object_or_404
from .models  import game
def prod(request, id):
    product = get_object_or_404(game, id=id)

    return render(request, 'product-details.html', {
        'product': product
    })
