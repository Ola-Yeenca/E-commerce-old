from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from item.models import Category, Item
from .forms import SignupForm
from django.core.paginator import Paginator

def index(request):
    items_list = Item.objects.filter(is_sold=False)
    paginator = Paginator(items_list, 6)  # Display 6 items per page

    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout(request):
    auth_logout(request)  # Perform the logout action
    return redirect('core:index')  # Redirect to the main page after logout
