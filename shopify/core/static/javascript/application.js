
var socket = new WebSocket("ws://" + window.location.host + "/ws/socket/");
socket.onmessage = function (event) {
    console.log("Received message from SocketConsumer:", event.data);
    // Handle the incoming message from SocketConsumer here
};



var notificationSocket = new WebSocket("ws://" + window.location.host + "/ws/notification/");
notificationSocket.onmessage = function (event) {
    console.log("Received message from NotificationConsumer:", event.data);
    // Handle the incoming message from NotificationConsumer here
};

// handle incoming messages
notificationSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    var notificationElement = document.createElement('div');
    notificationElement.classList.add('notification');
    notificationElement.innerText = message;
    document.querySelector('#notifications').append(notificationElement);
}
