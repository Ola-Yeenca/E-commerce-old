from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Conversation, ConversationMessage
from item.models import Item
from .forms import ConversationMessageForm

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversation = Conversation.objects.filter(item=item, member=request.user).first()

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            if not conversation:
                try:
                    conversation = Conversation.objects.create(item=item)
                    conversation.member.add(request.user)
                except Exception as e:
                    # Handle the conversation creation failure
                    error_message = "Failed to create a conversation. Please try again."
                    return render(request, 'conversation/error.html', {'error_message': error_message, 'conversation': None})

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.sender = request.user
            conversation_message.save()
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {'form': form, 'item': item, 'conversation': conversation})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(member=request.user)
    return render(request, 'conversation/inbox.html', {'conversations': conversations})