from django.contrib import admin

# Register your models here.

from .models import Item, Shop, Customer, ShopItem, Shopowner, Shopassigned, RequestedRent, DeleivaryMan,Invoice, OrderedItem,SalesManager,Review



admin.site.register(Item)
admin.site.register(Shop)
admin.site.register(Customer)
admin.site.register(ShopItem)
admin.site.register(Shopassigned)
admin.site.register(Shopowner)
admin.site.register(RequestedRent)
admin.site.register(DeleivaryMan)
admin.site.register(Invoice)
admin.site.register(OrderedItem)
admin.site.register(SalesManager)
admin.site.register(Review)


