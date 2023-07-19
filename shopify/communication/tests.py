from django.test import TestCase
import unittest
from unittest.mock import patch, MagicMock
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.http import Http404
from .models import Conversation, ConversationMessage
from item.models import Item
from .forms import ConversationMessageForm
from .views import new_conversation

class NewConversationTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.item = Item.objects.create(name='Test Item', created_by=self.user)
        self.conversation = Conversation.objects.create(item=self.item)
        self.conversation.members.add(self.user)
        self.form_data = {'message': 'Test message'}

    def test_new_conversation_redirect_if_item_created_by_user(self):
        request('/new_conversation/1')
        request.user = self.user
        response = new_conversation(request, self.item.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/index')

    def test_new_conversation_create_conversation_if_not_exists(self):
        request = self.factory.post('/new_conversation/1', data=self.form_data)
        request.user = self.user
        with patch('conversation.views.Conversation.objects.create') as mock_create:
            response = new_conversation(request, self.item.pk)
            mock_create.assert_called_once_with(item=self.item)

    def test_new_conversation_add_user_as_member(self):
        request = self.factory.post('/new_conversation/1', data=self.form_data)
        request.user = self.user
        with patch('conversation.views.Conversation.objects.create') as mock_create:
            response = new_conversation(request, self.item.pk)
            conversation = mock_create.return_value
            conversation.members.add.assert_called_once_with(self.user)

    def test_new_conversation_save_conversation_message(self):
        request = self.factory.post('/new_conversation/1', data=self.form_data)
        request.user = self.user
        with patch('conversation.views.ConversationMessageForm') as mock_form:
            form_instance = mock_form.return_value
            form_instance.is_valid.return_value = True
            response = new_conversation(request, self.item.pk)
            form_instance.save.assert_called_once_with(commit=False)

    def test_new_conversation_redirect_to_item_detail(self):
        request = self.factory.post('/new_conversation/1', data=self.form_data)
        request.user = self.user
        with patch('conversation.views.ConversationMessageForm') as mock_form:
            form_instance = mock_form.return_value
            form_instance.is_valid.return_value = True
            response = new_conversation(request, self.item.pk)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/item/detail/1')

    def test_new_conversation_render_error_page_on_conversation_creation_failure(self):
        request = self.factory.post('/new_conversation/1', data=self.form_data)
        request.user = self.user
        with patch('conversation.views.Conversation.objects.create') as mock_create:
            mock_create.side_effect = Exception('Test exception')
            response = new_conversation(request, self.item.pk)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'conversation/error.html')

    def test_new_conversation_render_new_page_on_get_request(self):
        request = self.factory.get('/new_conversation/1')
        request.user = self.user
        response = new_conversation(request, self.item.pk)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation/new.html')

    def test_new_conversation_render_new_page_with_form_on_get_request(self):
        request = self.factory.get('/new_conversation/1')
        request.user = self.user
        response = new_conversation(request, self.item.pk)
        self.assertIsInstance(response.context_data['form'], ConversationMessageForm)

    def test_new_conversation_render_new_page_with_item_on_get_request(self):
        request = self.factory.get('/new_conversation/1')
        request.user = self.user
        response = new_conversation(request, self.item.pk)
        self.assertEqual(response.context_data['item'], self.item)

    def test_new_conversation_render_new_page_with_conversation_on_get_request(self):
        request = self.factory.get('/new_conversation/1')
        request.user = self.user
        response = new_conversation(request, self.item.pk)
        self.assertEqual(response.context_data['conversation'], self.conversation)
