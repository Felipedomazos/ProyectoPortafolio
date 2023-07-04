function eliminarServicioCotizacion(itemId) {
  // Realizar una solicitud POST para eliminar el elemento del carrito
  fetch('/eliminar-servicio-cotizacion/', {
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
          text: 'Servicio eliminado de la cotización',
          icon: 'success',
          confirmButtonText: 'Aceptar'
        }).then(() => {
          row.remove();
        });
      }
    })
    .catch(error => {
      console.error(error);
    });
}

function buscarServicio() {
  var input = document.getElementById('bscr-serv');
  var filter = input.value.toUpperCase();
  var table = document.getElementsByClassName('tablaServicios')[0];
  var rows = table.getElementsByTagName('tr');

  for (var i = 0; i < rows.length; i++) {
    var td = rows[i].getElementsByTagName('td')[1];
    if (td) {
      var serviceName = td.textContent || td.innerText;
      if (serviceName.toUpperCase().indexOf(filter) > -1) {
        rows[i].style.display = '';
      } else {
        rows[i].style.display = 'none';
      }
    }
  }
}
