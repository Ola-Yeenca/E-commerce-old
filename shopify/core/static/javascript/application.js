function getWebSocketUrl(conversationId) {
  return `ws://${window.location.host}/ws/conversation/${conversationId}/`;
}

var conversationId = {{ conversation.id }};
var socketUrl = getWebSocketUrl(conversationId);
console.log("WebSocket URL:", socketUrl);

var socket = new WebSocket(socketUrl);

function handleNewMessage(data) {
  var newMessage = document.createElement('div');
  newMessage.innerHTML = `<div class="p-6 flex bg-gray-100 rounded-xl">
                             <div>
                               <p class="mb-4">
                                 <strong>${data.sender}</strong> @ ${data.timestamp}
                               </p>
                               <p>${data.message}</p>
                             </div>
                           </div>`;
  document.getElementById('conversation').appendChild(newMessage);
}

function handleNotification(data) {
  // Show a notification to the user
  // Example: display a notification banner or alert
  alert(data.message);
}

// Inside the socket.onmessage handler
socket.onmessage = function (event) {
  var data = JSON.parse(event.data);

  // Check the type of message and handle accordingly
  if (data.message_type === "new_message") {
    handleNewMessage(data);
  } else if (data.message_type === "notification") {
    handleNotification(data);
  }
};

document.getElementById("message-form").addEventListener("submit", function(event) {
  event.preventDefault();
  var content = document.getElementById("id_content").value;
  socket.send(JSON.stringify({
    'content': content
  }));
});

var socket = new WebSocket(socketUrl);

socket.onopen = function(event) {
  console.log("WebSocket connection opened:", event);
};

socket.onerror = function(error) {
  console.error("WebSocket error:", error);
};

socket.onclose = function(event) {
  console.log("WebSocket connection closed:", event);
};

// websocket.js

function setupWebSocket(conversationId) {
  var socket = new WebSocket('ws://' + window.location.host + `/ws/conversation/${conversationId}/`);

  socket.onmessage = function(event) {
    var message = JSON.parse(event.data);
    // Handle the incoming message and update the chat window
    // Example: Add the new message to the chat container
    var chatContainer = document.getElementById('chat-container');
    var newMessageElement = document.createElement('div');
    newMessageElement.textContent = message.sender + ': ' + message.message;
    chatContainer.appendChild(newMessageElement);
  };

  // Function to send a message through WebSocket
  function sendMessage(content) {
    var message = {
      content: content
    };
    socket.send(JSON.stringify(message));
  }
}

// Usage
// Call setupWebSocket(conversationId) in your HTML template to initialize WebSocket for each conversation
