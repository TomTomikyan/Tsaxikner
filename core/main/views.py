from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm, UserProfileForm,SupportForm
from .models import UserProfile, Category, Product, CartItem,Info,SupportMessage,Order,OrderItem

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                form.add_error(None, 'Incorrect username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    avatar_url = user_profile.avatar.url if user_profile.avatar else None
    cart_items = request.user.cart_items.all()
    
    return render(request, 'profile.html', {
        'user_profile': user_profile,
        'avatar_url': avatar_url,
        'cart_items': cart_items,
    })

@login_required
def edit_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('Profile') 
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})

def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product.html', {'products': products, 'categories': categories})

def product_detail(request, id):
    product_instance = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product_instance})

@login_required
def add_to_cart(request, product_id):
    product_instance = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product_instance)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
    return redirect('Cart')

@login_required
def view_cart(request):
    cart_items = request.user.cart_items.all()
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def order_success(request):
    return render(request, 'order_success.html')

@login_required
def checkout(request):
    cart_items = request.user.cart_items.all()
    if not cart_items:
        return redirect('Cart')
    
    total_price = sum(item.total_price for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)

    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.total_price)
        item.delete()  

    return redirect('OrderSuccess')

def info_view(request, id):
    product_info = get_object_or_404(Info, product_id=id)
    return render(request, 'info.html', {'product_info': product_info})

@login_required
def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            support_message = form.save(commit=False)
            support_message.user = request.user
            support_message.save()
            return redirect('SupportSuccess')
    else:
        form = SupportForm()


    return render(request, 'support.html', {'form': form})

@login_required
def support_success(request):
    return render(request, 'toshni.html')