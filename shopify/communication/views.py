from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, BooleanField
from .models import Conversation, ConversationMessage
from item.models import Item
from django.http import HttpResponseForbidden
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import user_passes_test


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversation = Conversation.objects.filter(item=item, members=request.user).first()

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            try:
                if not conversation:
                    conversation = Conversation.objects.create(item=item)
                    conversation.members.add(request.user)

                conversation_message = form.save(commit=False)
                conversation_message.conversation = conversation
                conversation_message.sender = request.user
                conversation_message.save()

                return redirect('item:detail', pk=item_pk)
            except Exception:
                # Handle conversation creation and message saving failure
                error_message = "Failed to create a conversation or save the message. Please try again."
                messages.error(request, error_message)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {'form': form, 'item': item, 'conversation': conversation})

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members=request.user)
    conversations = conversations.annotate(admin_in_members=Case(
        When(members=request.user, then=Value(True)),
        default=Value(False),
        output_field=BooleanField()
    ))
    conversations = Conversation.objects.all()
    for conversation in conversations:
        print('Conversation:', conversation)
        print('Members:', conversation.members.all())

    return render(request, 'conversation/inbox.html', {'conversations': conversations})


@login_required
def detail(request, conversation_pk):
    conversation = get_object_or_404(Conversation, pk=conversation_pk)

    if not (request.user in conversation.members.all()
            or request.user.is_superuser
            or request.user.is_staff):
        # return redirect('conversation:inbox')
        return HttpResponseForbidden("You are not authorized to access this page.")
    print('User:', request.user)
    print('Is Superuser or Staff:', request.user.is_superuser or request.user.is_staff)


    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.sender = request.user
            conversation_message.save()
            return redirect('conversation:detail', conversation_pk=conversation_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {'conversation': conversation, 'form': form})
