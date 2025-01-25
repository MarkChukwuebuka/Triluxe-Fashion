function makePaystackPayment() {
    const paystack = new PaystackPop();

    paystack.newTransaction({
        key: paystack_key,
        email: "m1@mailinator.com",
        amount:5000,

        onSuccess: (transaction) => {
            console.log(key);
            console.log(email);
            window.location.href = ""
        },

        onCancel: () => {

        }
    })
}