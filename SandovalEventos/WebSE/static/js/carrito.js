// Detalle Producto - cantidad
function incrementQuantity() {
  const quantityInput = document.getElementById('quantity');
  const currentQuantity = parseInt(quantityInput.value);
  quantityInput.value = currentQuantity + 1;
}
function decrementQuantity() {
  const quantityInput = document.getElementById('quantity');
  const currentQuantity = parseInt(quantityInput.value);

  if (currentQuantity > 1) {
    quantityInput.value = currentQuantity - 1;
  }
}

// Detalle Producto - Agregar al Carro
function addToCart(productId) {
  const quantityInput = document.getElementById('quantity');
  const quantity = parseInt(quantityInput.value);


  fetch('/agregar-al-carrito/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': '{{ csrf_token }}',
    },
    body: JSON.stringify({ productId: productId, quantity: quantity }),
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      Swal.fire({
        text: 'Producto añadido al carrito',
        icon: 'success',
        confirmButtonText: 'Aceptar'
      })
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Ocurrió un error al agregar el producto al carrito');
    });
}

// Carrito - Eliminar del Carro
function eliminarDelCarrito(itemId) {
  // Realizar una solicitud POST para eliminar el elemento del carrito
  fetch('/eliminar-del-carrito/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': '{{ csrf_token }}',  // Obtener el token CSRF
      },
      body: JSON.stringify({ itemId: itemId }),
  })
  .then(response => response.json())
  .then(data => {
      // Manejar la respuesta del servidor, por ejemplo, eliminar la fila correspondiente en la tabla del carrito
      if (data.success) {
        const row = document.getElementById(itemId);
        Swal.fire({
          title: 'Éxito',
          text: 'Producto eliminado del carrito',
          icon: 'success',
          confirmButtonText: 'Aceptar'
        }).then(() => {
          row.remove();
        });
      }
  })
  .catch(error => {
      // Manejar cualquier error
      console.error(error);
  });
}
