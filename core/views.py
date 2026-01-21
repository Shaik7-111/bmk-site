from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')


def products(request):
    category = request.GET.get('category')
    search_query = request.GET.get('q')
    view_mode = request.GET.get('view', 'grid')  # default = grid

    product_list = Product.objects.all()

    if category:
        product_list = product_list.filter(category=category)
    else:
        product_list = Product.objects.all().order_by('id')

    if search_query:
        product_list = product_list.filter(name__icontains=search_query)

    paginator = Paginator(product_list, 20)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'core/products.html', {
        'products': products,
        'selected_category': category,
        'search_query': search_query,
        'view_mode': view_mode,
    })


def contact(request):
    return render(request, 'core/contact.html')

def productdetail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'core/product-detail.html', {'product': product})


@login_required
def add_to_wishlist(request, product_id):
    Wishlist.objects.get_or_create(
        user=request.user,
        product_id=product_id
    )
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(
        user=request.user,
        product_id=product_id
    ).delete()
    return redirect('wishlist')

@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'core/wishlist.html', {
        'items': items
    })


from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin_once(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            "admin",
            "admin@example.com",
            "admin123"
        )
    return HttpResponse("Admin created")
