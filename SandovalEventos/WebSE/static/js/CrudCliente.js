function buscarUsuarios() {
    var input = document.getElementById('rut');
    var filter = input.value.toUpperCase();
    var table = document.getElementById('tabla-usuarios');
    var rows = table.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var rutColumn = rows[i].getElementsByTagName('td')[0];
        if (rutColumn) {
            var rutText = rutColumn.textContent || rutColumn.innerText;
            if (rutText.toUpperCase().indexOf(filter) > -1) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    }
}

function editarUsuario(id) {
    // Lógica para editar el usuario con el ID proporcionado
    console.log('Editar usuario:', id);
}

function eliminarUsuario(id) {
    // Lógica para eliminar el usuario con el ID proporcionado
    console.log('Eliminar usuario:', id);
}