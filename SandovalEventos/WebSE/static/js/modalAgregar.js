const myModal = document.querySelector('#mymodal');
myModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const heading = button.getAttribute('data-bs-heading');


    const title = myModal.querySelector('.modal-header').textContent =
          heading;
});


const selectCotizacion = document.getElementById("select-cotizacion");
const nombreCotizacion = document.getElementById("nombre-cotizacion");
const inputNombreCotizacion = document.getElementById("input-nombre-cotizacion");


selectCotizacion.addEventListener("change", function() {
  if (selectCotizacion.value === "nueva-cotizacion") {
    nombreCotizacion.style.display = "block";
  } else {
    nombreCotizacion.style.display = "none";
  }
});
