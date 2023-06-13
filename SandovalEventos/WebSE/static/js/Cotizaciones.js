var crearCotizacionLink = document.getElementById("crearCotizacion");

var modal = document.getElementById("modalCrearCotizacion");

var closeButton = document.getElementById("closeModal");

function openModal() {
  modal.style.display = "block";
}
function closeModal() {
  modal.style.display = "none";
}

crearCotizacionLink.addEventListener("click", openModal);

closeButton.addEventListener("click", closeModal);

document.addEventListener('DOMContentLoaded', function() {
  var messageContainer = document.querySelector('.messages');
  if (messageContainer) {
      setTimeout(function() {
          messageContainer.style.opacity = '0';
          setTimeout(function() {
              messageContainer.style.display = 'none';
          }, 1000);
      }, 3000);
  }
});