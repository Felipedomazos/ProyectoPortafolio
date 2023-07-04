const myModal = document.querySelector('#mymodal');
let precioServ;

myModal.addEventListener('show.bs.modal', function (event) {
  const button = event.relatedTarget;
  const heading = button.getAttribute('data-bs-heading');
  precioServ = parseFloat(button.getAttribute('data-bs-precio'));
  const title = myModal.querySelector('.modal-header').textContent = heading;
  const precioElement = myModal.querySelector('.modal-precio');
  precioElement.textContent = formatPrice(precioServ);
});
const selectCotizacion = document.getElementById("select-cotizacion");
const cantidadInput = document.getElementById('cantidad');

function calcularPrecioTrago() {
  const cantidad = cantidadInput.value;
  const precioCalculado = cantidad * precioServ;
  const precioElement = document.querySelector('.modal-precio');
  precioElement.textContent = formatPrice(precioCalculado);
} 

function formatPrice(price) {
  return price.toLocaleString('es-CL', { style: 'currency', currency: 'CLP' });
}

var botonCerrar = myModal.querySelector('.btn-danger');
botonCerrar.addEventListener('click', restablecerModal);

// Función para restablecer el modal
function restablecerModal() {
  myModal.classList.remove('show'); 
  myModal.style.display = 'none'; 
  myModal.style.opacity = '';

  var selectCotizacion = document.getElementById('select-cotizacion');
  selectCotizacion.value = 'seleccionCotizacion';

  var cantidad = document.getElementById('cantidad');
  cantidad.value = '1';

  selectCotizacion.classList.remove('is-invalid');
  cantidad.classList.remove('is-invalid');
}
