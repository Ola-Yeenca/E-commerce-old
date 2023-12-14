from django.shortcuts import render
from django.conf import settings

# Create your views here.

from django.http import JsonResponse

def checkout(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        # Process payment using the token
        # You can use the Stripe API to create a charge or save the token for later use
        return JsonResponse({'message': 'Payment successful'})
    return render(request, 'checkout.html', {'stripe_public_key': settings.STRIPE_PUBLIC_KEY})

