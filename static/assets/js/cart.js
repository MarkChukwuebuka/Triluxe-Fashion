// Check if button pressed
$(document).on('click', '#add-cart', function(e){
    e.preventDefault();
    const url = $(this).data('url');
    const productId = $(this).val();
    const productQty = $('#qty-cart').val();

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            product_id: $('#add-cart').val(),
            product_qty: productQty,
            csrfmiddlewaretoken: csrfToken,
            action: 'post'
        },

        success: function(json){
            console.log(json)
            document.getElementById("cart_quantity").textContent = json.qty
            location.reload();
        },

        error: function(xhr, errmsg, err){

        }
    });
})


// Update Cart
//$(document).on('click', '.update-cart', function(e){
//  e.preventDefault();
//  // grab the product id
//  var productid = $(this).data('index');
//
//  $.ajax({
//  type: 'POST',
//  url: '{% url 'cart_update' %}',
//  data: {
//    product_id: $(this).data('index'),
//    product_qty: $('#select' + productid + ' option:selected').text(),
//    csrfmiddlewaretoken: '{{ csrf_token }}',
//    action: 'post'
//  },
//  success: function(json){
//      //console.log(json)
//      //document.getElementById("cart_quantity").textContent = json.qty
//      location.reload();
//  },
//
//  error: function(xhr, errmsg, err){
//
//  }
//
//
//  });
//
//})
//
//// Delete Item From Cart
//$(document).on('click', '.delete-product', function(e){
//  e.preventDefault();
//  // grab the product id
//  //var productid = $(this).data('index');
//
//  $.ajax({
//  type: 'POST',
//  url: '{% url 'cart_delete' %}',
//  data: {
//    product_id: $(this).data('index'),
//    csrfmiddlewaretoken: '{{ csrf_token }}',
//    action: 'post'
//  },
//  success: function(json){
//      //console.log(json)
//      //document.getElementById("cart_quantity").textContent = json.qty
//      location.reload();
//  },
//
//  error: function(xhr, errmsg, err){
//
//  }
//
//
//  });
//
//})
