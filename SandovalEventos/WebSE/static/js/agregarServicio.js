$(document).ready(function () {
    $('.agregarButton').click(function() {
        var nombreServicio = $(this).data('nombre-servicio');
        $('#nombre-servicio').val(nombreServicio);
    });

    $('#select-cotizacion').change(function () {
        var cotizacionSeleccionada = $(this).val();
        var nombreCotizacion = '';
        if (cotizacionSeleccionada === 'nueva-cotizacion') {
            nombreCotizacion = $('#input-nombre-cotizacion').val();
        } else {
            nombreCotizacion = $('#select-cotizacion option:selected').text();
        }

        $('#cotizacionSeleccionada').val(cotizacionSeleccionada);
        $('#nombreCotizacion').val(nombreCotizacion);
    });

    $('#btn-agregar').click(function () {
        var nombreServicio = $('#nombre-servicio').val();
        var cantidad = $('#cantidad').val();
        var precio = $('#mymodal').data('bs-precio');
        var cotizacionSeleccionada = $('#cotizacionSeleccionada').val().toString();
        var nombreCotizacion = $('#nombreCotizacion').val();

        $.ajax({
            url: '/agregar-servicio-cotizacion/', 
            type: 'POST',
            data: {
                nombre_servicio: nombreServicio,
                cantidad: cantidad,
                precio: precio,
                cotizacion: cotizacionSeleccionada,
                nombre_cotizacion: nombreCotizacion
            },
            success: function (response) {
                Swal.fire({
                    title: 'Éxito',
                    text: 'Servicio agregado a la cotización con éxito.',
                    icon: 'success',
                    confirmButtonText: 'Aceptar'
                }).then(function () {
                    window.location.reload();
                    $('#modal-form').trigger('reset');
                });
            },
            error: function (xhr, errmsg, err) {
                Swal.fire({
                    title: 'Error',
                    text: 'Seleccione una cotización para agrear el servicio.',
                    icon: 'error',
                    confirmButtonText: 'Aceptar'
                });
            }
        });
    });
});