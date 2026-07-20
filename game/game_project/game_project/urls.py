from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('shop/', include('shop_app.urls')),
    path('product/<int:id>/', views.product_detail, name='prod'),
    path('contact/', views.contact, name='contect'),
    path('', include('login_app.urls')),
    path('', include('new_game_app.urls')),
    path('', include('coment_app.urls')),
    path('sabad/', views.sabad, name='sabad'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('shop-add-to-cart/<int:id>/', views.add_shop_to_cart, name='add_shop_to_cart'),
    path('cart/remove/<int:id>/', views.cart_remove, name='cart_remove'),
    path('cart/increase/<int:id>/', views.cart_increase, name='cart_increase'),
    path('cart/decrease/<int:id>/', views.cart_decrease, name='cart_decrease'),
    path('checkout/', views.checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)