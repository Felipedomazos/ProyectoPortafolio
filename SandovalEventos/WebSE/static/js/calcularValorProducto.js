const precioUnitario = 400; // Precio unitario de cada producto
const cantidadInput = document.getElementById('cantidad');
const precioInput = document.getElementById('precio');
const inputPrecioServ = document.getElementById("precioServ");

function calcularPrecio() {
  const cantidad = cantidadInput.value;
  const precio = cantidad * precioUnitario;
  precioInput.value = precio;
}


inputPrecioServ.value = "15.990";