function openCity(evt, cityName) {
    var i, tabcontentCuenta, tablinks;
    tabcontentCuenta = document.getElementsByClassName("tabcontentCuenta");
    for (i = 0; i < tabcontentCuenta.length; i++) {
        tabcontentCuenta[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();


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