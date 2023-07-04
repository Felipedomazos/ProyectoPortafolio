var rutInput = document.getElementById('rut');
var nombreInput = document.getElementById('nombre');
var apellidoInput = document.getElementById('apellido');
var correoInput = document.getElementById('correo');
var fonoInput = document.getElementById('fono');
var direccionInput = document.getElementById('direccion');
var contraseñaInput = document.getElementById('contraseña');
    
var guardarButton = document.getElementById('guardar-button');
    
rutInput.addEventListener('input', habilitarBoton);
nombreInput.addEventListener('input', habilitarBoton);
apellidoInput.addEventListener('input', habilitarBoton);
correoInput.addEventListener('input', habilitarBoton);
fonoInput.addEventListener('input', habilitarBoton);
direccionInput.addEventListener('input', habilitarBoton);
contraseñaInput.addEventListener('input', habilitarBoton);
    
function habilitarBoton() {
    guardarButton.disabled = false;
}

var contraseñaInput = document.getElementById('contraseña');
var togglePassword = document.getElementById('toggle-password');

function togglePasswordVisibility() {
    if (contraseñaInput.type === 'password') {
        contraseñaInput.type = 'text';
    } else {
        contraseñaInput.type = 'password';
    }
}

$(document).ready(function () {
    $('#cliente-form').on('submit', function (event) {
        event.preventDefault(); // Evita que se envíe el formulario de forma predeterminada

        // Captura los valores de los campos del formulario
        var nombre = $('#nombre').val();
        var apellido = $('#apellido').val();
        var correo = $('#correo').val();
        var fono = $('#fono').val();
        var direccion = $('#direccion').val();
        var contraseña = $('#contraseña').val();

        // Crea un objeto con los valores capturados
        var data = {
            nombreCliente: nombre,
            apellidoCliente: apellido,
            correoCliente: correo,
            fonoCliente: fono,
            direccionCliente: direccion,
            contraseñaCliente: contraseña
        };

        // Envía una solicitud POST al servidor para actualizar los datos del cliente
        $.ajax({
            url: '/ruta-de-actualizacion',  // Reemplaza '/ruta-de-actualizacion' con la URL adecuada de tu aplicación
            type: 'POST',
            data: data,
            success: function (response) {
                // Maneja la respuesta del servidor después de actualizar los datos
                console.log('Datos actualizados correctamente');
                // Realiza cualquier acción adicional requerida
            },
            error: function (error) {
                // Maneja los errores en caso de que ocurra alguno
                console.log('Error al actualizar los datos');
                // Realiza cualquier acción adicional requerida
            }
        });
    });
});