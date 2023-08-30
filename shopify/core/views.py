from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from item.models import Category, Item
from .forms import SignupForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

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

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email=settings.EMAIL_HOST_USER,
                email_template_name='core/password_reset_email.html',
                subject_template_name='core/password_reset_subject.txt',
                html_email_template_name='core/password_reset_email.html',
            )
            messages.success(request, 'Password reset email sent.')
            return redirect('core:password_reset_done') # Redirect to the reset_password_done view
        else:
            messages.error(request, 'Error processing request.')
    else:
        form = PasswordResetForm()
    return render(request, 'core/reset_password.html', {'form': form})

def reset_password_done(request):
    return render(request, 'core/password_reset_done.html')

def reset_password_confirm(request, uidb64, token):
    return render(request, 'core/password_reset_confirm.html')

def reset_password_complete(request):
    return render(request, 'core/password_reset_complete.html')

