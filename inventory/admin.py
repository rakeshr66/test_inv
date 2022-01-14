from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from .models import UsersDetails, Category, Product, SubCategory, SubCatModel, ProductBrand, Order

admin.site.register(UsersDetails)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(SubCatModel)
admin.site.register(ProductBrand)
admin.site.register(Order)





