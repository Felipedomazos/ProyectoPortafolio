const precioUnitario = 700; // Precio unitario de cada producto
const cantidadInput = document.getElementById('cantidad');
const precioInput = document.getElementById('precio');


function calcularPrecio() {
  const cantidad = cantidadInput.value;
  const precio = cantidad * precioUnitario;
  precioInput.value = precio;
}
