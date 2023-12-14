from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, CartItem
from django.contrib import messages

# Create your views here.
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    messages.success(request, f'Added {item.name} to your cart')
    request.session['cart'] = cart
    return redirect('shopify:item_detail', pk=item_id)

def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart/view_cart.html', {'cart': cart})

def adjust_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {item_id} quantity to {quantity}')
    else:
        cart.pop(item_id, None)
        messages.success(request, f'Removed {item_id} from your cart')
    request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart.pop(item_id, None)
    messages.success(request, f'Removed {item_id} from your cart')
    request.session['cart'] = cart
    return redirect('view_cart')

def checkout(request):
    return render(request, 'cart/checkout.html')
