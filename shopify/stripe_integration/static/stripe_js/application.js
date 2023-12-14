// application.js

var stripe = Stripe('{{ stripe_public_key }}');
var elements = stripe.elements();

var card = elements.create('card');
card.mount('#card-element');

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    stripe.createToken(card).then(function (result) {
        if (result.error) {
            // Display error to the user
            console.error(result.error.message);
        } else {
            // Send token to your server
            stripeTokenHandler(result.token);
        }
    });
});

function stripeTokenHandler(token) {
    // You can send the token to your server here
    console.log(token);
}
