from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView,DeleteView
from .forms import LoginForm, AddUserForm, EditUserForm, ProductForm, OrderSupplyForm, OrderForm
from .models import *


class HomeView(TemplateView):
    template_name = "blog_temp/pages/home.html"


class LoginPageView(TemplateView):
    # login url is set in settings.py
    # logout url set in header - same as login url
    template_name = "blog_temp/pages/login.html"
    form_class = LoginForm

    def get_context_data(self, request):
        context = {}
        context['redirect_to_url'] = request.GET.get('next', reverse(
            'inv_user_list'))  # hidden redirect url
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # logout if user already logged in
            print("logging out current user")
            logout(request)
        return render(request, self.template_name, context=self.get_context_data(request=request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        post_data = request.POST
        url_redirect = post_data.get('next', reverse('inv_user_list'))
        if form.is_valid():
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user=user)  # save user to session to access inner pages
                # if url_redirect == reverse('home'):
                # if request.user.usersdetails.type.name == 'user':
                #     url_redirect = reverse('home')
                # elif request.user.usersdetails.type.name == 'admin':
                url_redirect = reverse('inv_user_list')
                return HttpResponseRedirect(url_redirect)

        context = self.get_context_data(request=request)
        context['error'] = 'Username or Password invalid!!'
        return render(request, self.template_name, context=context)


class UsersListAddView(LoginRequiredMixin, CreateView):
    template_name = "registrations/users/user_add.html"
    form_class = AddUserForm
    success_url = reverse_lazy('inv_user_list')
    model = UsersDetails

    def get_context_data(self, **kwargs):
        context = super(UsersListAddView, self).get_context_data(**kwargs)
        context['active_user'] = "active"  # sidebar active tag
        context['active_user_add'] = "active"
        return context

    def form_valid(self, form):
        # if form.is_valid():
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Added successfully!!")
        return super(UsersListAddView, self).form_valid(form)


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'registrations/users/user_edit.html'
    model = UsersDetails
    form_class = EditUserForm

    def get_success_url(self):
        id = self.kwargs['id']
        return reverse('inv_user_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            # messages.add_message(self.request, messages.SUCCESS, "Edited successfuly!!")
        return super(UsersUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UsersUpdateView, self).get_context_data(**kwargs)
        context['active_user'] = "active"
        context['active_user_list'] = "active"  # sidebar active tag
        usersdetails = self.get_object()
        form_init = model_to_dict(usersdetails)
        form_init['email'] = usersdetails.user.email
        form = self.form_class(initial=form_init)
        context['form'] = form
        context['id'] = usersdetails.id
        return context

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return UsersDetails.objects.get(id=id)


class UsersListView(LoginRequiredMixin, ListView):
    template_name = 'registrations/users/users_list.html'
    model = UsersDetails

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UsersDetailView(LoginRequiredMixin, DetailView):
    template_name = 'registrations/users/user_detail.html'
    model = UsersDetails
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.object.status
        if status == '1':
            context['stat'] = 'active'
        else:
            context['stat'] = 'inactive'
        return context


class UsersDeleteView(LoginRequiredMixin, DeleteView):
    model = UsersDetails
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        userdtl = UsersDetails.objects.get(pk=id)
        userauth = User.objects.get(email=userdtl.email)
        userauth.delete()
        return HttpResponseRedirect(reverse('inv_user_list'))


class ProductCategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'


class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'category/subcategory_list.html'


class ProductBrandListView(ListView):
    model = ProductBrand
    template_name = 'category/brand_ist.html'


class SubCatModelListView(ListView):
    model = SubCatModel
    template_name = 'category/model_list.html'


class ProductCategoryAddView(CreateView):
    model = Category
    template_name = 'category/category_add.html'
    fields = ['categoryname', 'description']

    def get_success_url(self):
        return reverse_lazy('inv_categ_list')


class SubCategoryAddView(CreateView):
    model = SubCategory
    template_name = 'category/category_add.html'
    fields = ['categname', 'subcategoryname', 'subdescription']

    def get_success_url(self):
        return reverse_lazy('inv_subcateg_list')


class ProductBrandAddView(CreateView):
    model = ProductBrand
    template_name = 'category/category_add.html'
    fields = ['categorynamebran', 'subcatname', 'brandname']

    def get_success_url(self):
        return reverse_lazy('inv_productbran_list')


class SubCatModelAddView(CreateView):
    model = SubCatModel
    template_name = 'category/category_add.html'
    fields = ['categorynamemod', 'subcatename', 'branname', 'prodmodelname', 'modeldescription']

    def get_success_url(self):
        return reverse_lazy('inv_subcatemodel_list')


class CategoryDeleteView(DeleteView):
    model = Category

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('inv_categ_list')


class SubCategoryDeleteView(DeleteView):
    model = SubCategory

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('inv_subcateg_list')


class ProductBrandDeleteView(DeleteView):
    model = ProductBrand

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('inv_productbran_list')


class SubCatModelDeleteView(DeleteView):
    model = SubCatModel

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('inv_subcatemodel_list')


def create_product(request):
    form = ProductForm(request.POST or None)
    product = Product.objects.all()
    if request.method == "POST":
        if form.is_valid():
            # book = form.save(commit=False)
            # book.author = author
            product = form.save(commit=False)
            product.save()
        else:
            return render(request, "product/partials/book_form.html", context={
                "form": form
            })

    context = {
        "form": form,
        # "author": author,
        "product": product
    }

    return render(request, "product/create_book.html", context)


def product_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("inv_product_add")
    context = {
        "form": form,
        "product": product
    }

    return render(request, "product/partials/book_form.html", context)


def product_delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST":
        product.delete()
        return redirect('inv_product_add')

    context = {
        "form": form,
        "product": product
    }
    return render(request, 'product/product_delete.html', context)


def order_supply_create(request):
    supply = OrderSupply.objects.all()
    form = OrderSupplyForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('inv_supply_create')

    context = {
        'supply': supply,
        'form': form
    }
    return render(request, 'product/order_supply_create.html', context)


def order_supply_edit(request, pk):
    supply = OrderSupply.objects.get(id=pk)
    form = OrderSupplyForm(request.POST or None, instance=supply)
    if form.is_valid():
        if request.method == 'POST':
            form.save()
            return redirect('inv_supply_create')

    context = {
        'form': form,
        'supply': supply
    }
    return render(request, 'product/order_supply_edit.html', context)


def order_supply_delete(request, pk):
    supply = get_object_or_404(OrderSupply, id=pk)
    form = OrderSupplyForm(request.POST or None, instance=supply)
    if request.method == 'POST':
        supply.delete()
        return redirect('inv_supply_create')
    context = {
        'form': form,
        'supply': supply
    }
    return render(request, 'product/order_supply_delete.html', context)


def order_create(request):
    form = OrderForm(request.POST or None)
    order = Order.objects.all()
    print(order)
    if request.method == "POST":
        form.save()
        return redirect("inv_order_create")
    context = {
        'form': form,
        'order': order
    }
    return render(request, 'order/order_create.html', context)

