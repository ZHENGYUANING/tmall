
from django.contrib import admin

from .models import Product


# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid','name', 'price', 'stock', 'sku','addtime']
    # list_filter = [ 'created']
    # list_editable = ['price', 'stock', 'available']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


# def save(self, *args, **kwargs):
#     if not self.slug:
#         self.slug = slugify(self.name)
#     super(Product, self).save(*args, **kwargs)

