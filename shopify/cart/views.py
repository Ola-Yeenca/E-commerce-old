from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def add_to_cart(request, item_id):
    # Implement logic to add the item to the cart
    pass  # TODO: implement this
    messages.success(request, 'Item added to cart successfully.')
    return redirect('cart:view_cart')

def view_cart(request):

    # Implement logic to retrieve and display the items in the cart
    return render(request, 'cart/view_cart.html')

def checkout(request):
    # Implement logic for the checkout process
    return render(request, 'cart/checkout.html')

