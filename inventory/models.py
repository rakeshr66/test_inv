from django.contrib.auth.models import User, Group
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.


class UsersDetails(models.Model):
    Active = '1'
    Inactive = '0'
    active_type = (
        (Active, 'Active'),
        (Inactive, 'Inactive'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    current_address = models.CharField(max_length=250, blank=True, default="-NA-")
    email = models.EmailField(max_length=90, default='')
    phone_regex = RegexValidator(regex = '^[6-9]\d{9}$',
                                 message="Phone number must be entered in the format")
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True,)  # validators should be a list
    type = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.CharField(choices=active_type, max_length=100, default="1")

    def __str__(self):
        return self.name


class Category(models.Model):
    categoryname = models.CharField(max_length=40, default='')
    description = models.TextField(max_length=40, blank=True)

    def __str__(self):
        return self.categoryname


class SubCategory(models.Model):
    categname = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100, default='')
    subcategoryname = models.CharField(max_length=40, default='')
    subdescription = models.TextField(max_length=40, blank=True)

    def __str__(self):
        return self.subcategoryname


class ProductBrand(models.Model):
    categorynamebran = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100, default='')
    subcatname = models.ForeignKey(SubCategory, on_delete=models.CASCADE, max_length=100, default='')
    brandname = models.CharField(max_length=60)

    def __str__(self):
        return self.brandname


class SubCatModel(models.Model):
    categorynamemod = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100, default='')
    subcatename = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default='')
    branname = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, max_length=100, default='')
    prodmodelname = models.CharField(max_length=60)
    modeldescription = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.prodmodelname


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default='')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, default='')
    productbrand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True, default='')
    productmodel = models.ForeignKey(SubCatModel, on_delete=models.SET_NULL, null=True, default='')
    productname = models.CharField(max_length=40)
    productunit = models.IntegerField()
    pricebuy = models.FloatField()
    pricesell = models.FloatField()
    productdescri = models.CharField(max_length=40, blank=True)
    productaddedby = models.CharField(blank=True, default='', max_length=60)
    prouctdateadded = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.productname


class OrderSupply(models.Model):
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    qty = models.IntegerField()
    orderedat = models.DateTimeField(auto_now_add=True, blank=True)
    arrivedat = models.DateTimeField(blank=True,null=True)
    arrived = models.BooleanField()


class Order(models.Model):
    orderid = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    productorder = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    orderunitprice = models.FloatField()
    ordersize = models.FloatField(max_length=40)
    orderqty = models.IntegerField()
    orderdiscount = models.FloatField()
    cgst = models.FloatField()
    sgst = models.FloatField()
    ordertotal = models.FloatField()
    orderdate = models.DateTimeField(auto_now_add=True, blank=True)
    orderdtl = models.TextField(max_length=40)
    status = models.BooleanField()
    ordergenerate = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name='staff')

    def __str__(self):
        return str(self.productorder)