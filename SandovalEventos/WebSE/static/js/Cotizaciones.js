var crearCotizacionLink = document.getElementById("crearCotizacion");
var eliminarCotizacionLink = document.getElementById("eliminarCotizacion");
var modalCrearCotizacion = document.getElementById("modalCrearCotizacion");
var modalEliminarCotizacoin = document.getElementById("modalEliminarCotizacion");
var closeButtonCC = document.getElementById("closeModalCC");
var closeButtonEC = document.getElementById("closeModalEC");

function openModalCC() {
  modalCrearCotizacion.style.display = "block";
}
function openModalEC() {
  modalEliminarCotizacoin.style.display = "block";
}
function closeModalCC() {
  modalCrearCotizacion.style.display = "none";
}
function closeModalEC() {
  modalEliminarCotizacoin.style.display = "none";
}

crearCotizacionLink.addEventListener("click", openModalCC);
eliminarCotizacionLink.addEventListener("click", openModalEC);
closeButtonCC.addEventListener("click", closeModalCC);
closeButtonEC.addEventListener("click", closeModalEC)

document.addEventListener('DOMContentLoaded', function () {
  var messageContainer = document.querySelector('.messages');
  if (messageContainer) {
    setTimeout(function () {
      messageContainer.style.opacity = '0';
      setTimeout(function () {
        messageContainer.style.display = 'none';
      }, 1000);
    }, 3000);
  }
});

document.getElementById("eliminarCotizacionForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada

  // Obtén los datos del formulario
  var form = event.target;
  var formData = new FormData(form);
  var nombreCotizacion = document.getElementById("select-elim-coti").options[document.getElementById("select-elim-coti").selectedIndex].text;

  // Mostrar cuadro de diálogo de confirmación antes de eliminar
  Swal.fire({
    title: "¿Estás seguro de eliminar la cotización '" + nombreCotizacion + "'?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Eliminar",
    cancelButtonText: "Cancelar",
    reverseButtons: true
  }).then((result) => {
    if (result.isConfirmed) {
      // Realiza la solicitud de eliminación utilizando AJAX
      var xhr = new XMLHttpRequest();
      xhr.open("POST", form.action);
      xhr.setRequestHeader("X-CSRFToken", formData.get("csrfmiddlewaretoken")); // Asegúrate de tener el token CSRF disponible en el formulario
      xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            Swal.fire({
              icon: 'success',
              title: 'Cotización eliminada correctamente',
              showConfirmButton: false,
              timer: 1500
            }).then(() => {
              window.location.reload();
            });
          } else {
            Swal.fire({
              icon: 'error',
              title: 'Error al eliminar la cotización',
              text: 'Ha ocurrido un error al eliminar la cotización',
              confirmButtonText: 'Aceptar'
            });
          }
        }
      };
      xhr.send(formData);
    }
  });
});