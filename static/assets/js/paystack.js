function makePaystackPayment() {
    const paystack = new PaystackPop();

    paystack.newTransaction({
        key: paystack_key,
        email: "",
        amount:"",

        onSuccess: (transaction) => {
            console.log(transaction);
            window.location.href = ""
        },

        onCancel: () => {

        }
    })
}