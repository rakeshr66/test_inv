from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='inventory_home'),
    url(r'login/$', LoginPageView.as_view(), name='inventory_login'),
    url(r'home/$', HomeView.as_view(), name='home'),
    url(r'users/add/$', UsersListAddView.as_view(), name='inv_user_add'),
    url(r'users/edit/(?P<id>\d+)$', UsersUpdateView.as_view(), name='inv_user_edit'),
    url(r'users/list/$', UsersListView.as_view(), name='inv_user_list'),
    url(r'user/(?P<id>\d+)/details$', UsersDetailView.as_view(), name='inv_user_details'),
    url(r'users/delete/(?P<pk>\d+)$', UsersDeleteView.as_view(), name='inv_user_del'),

    url(r'category/list/$', ProductCategoryListView.as_view(), name='inv_categ_list'),
    url(r'category/sub/list/$', SubCategoryListView.as_view(), name='inv_subcateg_list'),
    url(r'brands/list/$', ProductBrandListView.as_view(), name='inv_productbran_list'),
    url(r'model/list/$', SubCatModelListView.as_view(), name='inv_subcatemodel_list'),

    url(r'category/add/$', ProductCategoryAddView.as_view(), name='inv_categ_add'),
    url(r'category/sub/add/$', SubCategoryAddView.as_view(), name='inv_subcateg_add'),
    url(r'brands/add/$', ProductBrandAddView.as_view(), name='inv_productbran_add'),
    url(r'model/add/$', SubCatModelAddView.as_view(), name='inv_subcatemodel_add'),

    url(r'category/(?P<pk>\d+)/delete$', CategoryDeleteView.as_view(), name='inv_categ_del'),
    url(r'category/sub/(?P<pk>\d+)/delete$', SubCategoryDeleteView.as_view(), name='inv_subcateg_del'),
    url(r'brands/(?P<pk>\d+)/delete$', ProductBrandDeleteView.as_view(), name='inv_brands_del'),
    url(r'model/(?P<pk>\d+)/delete$', SubCatModelDeleteView.as_view(), name='inv_model_del'),

    url(r'product/add/$', create_product, name='inv_product_add'),
    url(r'product/update/(?P<pk>\d+)$', product_update, name='inv_product_update'),
    url(r'product/delete/(?P<pk>\d+)$', product_delete, name='inv_product_delete'),

    url(r'order/supply/create/$', order_supply_create, name='inv_supply_create'),
    url(r'order/supply/update/(?P<pk>\d+)$', order_supply_edit, name='inv_supply_edit'),
    url(r'order/supply/delete/(?P<pk>\d+)$', order_supply_delete, name='inv_supply_delete'),

    url(r'order/create/$', order_create, name='inv_order_create'),



]
