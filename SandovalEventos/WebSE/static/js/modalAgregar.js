const myModal = document.querySelector('#mymodal');
myModal.addEventListener('show.bs.modal', function (event) {
  const button = event.relatedTarget;
  const heading = button.getAttribute('data-bs-heading');
  const title = myModal.querySelector('.modal-header').textContent = heading;
});
const selectCotizacion = document.getElementById("select-cotizacion");
const nombreCotizacion = document.getElementById("nombre-cotizacion");
const inputNombreCotizacion = document.getElementById("input-nombre-cotizacion");

selectCotizacion.addEventListener("change", function () {
  if (selectCotizacion.value === "nueva-cotizacion") {
    nombreCotizacion.style.display = "block";
  } else {
    nombreCotizacion.style.display = "none";
  }
});





// Modal Servicio
const myModalServ = document.querySelector('#mymodalServ');
myModalServ.addEventListener('show.bs.modal', function (event) {
  const button = event.relatedTarget;
  const heading = button.getAttribute('data-bs-heading');
  const title = myModalServ.querySelector('.modal-header').textContent = heading;
});
const selectCotizacionServ = document.getElementById("select-cotizacion-serv");
const nombreCotizacionServ = document.getElementById("nombre-cotizacion-serv");
const inputNombreCotizacionServ = document.getElementById("input-nombre-cotizacion-serv");

selectCotizacionServ.addEventListener("change", function () {
  if (selectCotizacionServ.value === "nueva-cotizacion") {
    nombreCotizacionServ.style.display = "block";
  } else {
    nombreCotizacionServ.style.display = "none";
  }
});





var botonCerrar = myModal.querySelector('.btn-danger');
botonCerrar.addEventListener('click', restablecerModal);

var botonAgregar = myModal.querySelector('.btn-success');
botonAgregar.addEventListener('click', restablecerModal);

// Función para restablecer el modal
function restablecerModal() {
  myModal.classList.remove('show'); 
  myModal.style.display = 'none'; 
  myModal.style.opacity = ''; 

  var selectCotizacion = document.getElementById('select-cotizacion');
  selectCotizacion.value = 'seleccionCotizacion';

  var nombreCotizacion = document.getElementById('input-nombre-cotizacion');
  nombreCotizacion.value = '';

  var cantidad = document.getElementById('cantidad');
  cantidad.value = '';

  var precio = document.getElementById('precio');
  precio.value = '';

  selectCotizacion.classList.remove('is-invalid');
  nombreCotizacion.classList.remove('is-invalid');
  cantidad.classList.remove('is-invalid');
}
