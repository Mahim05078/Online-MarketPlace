from django.contrib import admin

# Register your models here.

from .models import Item, Shop, Customer, ShopItem, Shopowner, Shopassigned


admin.site.register(Item)
admin.site.register(Shop)
admin.site.register(Customer)
admin.site.register(ShopItem)
admin.site.register(Shopassigned)
admin.site.register(Shopowner)
