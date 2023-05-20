const searchInput = document.getElementById('searchInput');
const checkboxes = document.querySelectorAll('.opcTragos input[type="checkbox"]');
const filterCheckboxes = document.querySelectorAll('.opcFiltros input[type="checkbox"]');

searchInput.addEventListener('input', function () {
    const searchTerm = searchInput.value.toLowerCase();
    checkboxes.forEach(function (checkbox) {
        const label = checkbox.parentNode;
        const optionText = label.textContent.toLowerCase();
        if (optionText.includes(searchTerm)) {
            label.style.display = 'block';
        } else {
            label.style.display = 'none';
        }
    });
});

searchInput.addEventListener('input', function () {
    filterOptions();
});

filterCheckboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        filterOptions();
    });
});

function filterOptions() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedFilters = Array.from(filterCheckboxes)
        .filter(function (checkbox) {
            return checkbox.checked;
        })
        .map(function (checkbox) {
            return checkbox.name;
        });

    checkboxes.forEach(function (checkbox) {
        const label = checkbox.parentNode;
        const optionText = label.textContent.toLowerCase();
        const optionTags = checkbox.value.toLowerCase().split(' ');

        const matchesSearchTerm = optionText.includes(searchTerm);
        const matchesFilters = selectedFilters.length === 0 || optionTags.some(function (tag) {
            return selectedFilters.includes(tag);
        });

        if (matchesSearchTerm && matchesFilters) {
            label.style.display = 'block';
        } else {
            label.style.display = 'none';
        }
    });
}

// Obtener todos los elementos con la clase "opcTragos"
var opcionesTragos = document.querySelectorAll('.opcTragos input[type="checkbox"]');

// Agregar un evento de escucha a cada checkbox
opcionesTragos.forEach(function(opcion) {
    opcion.addEventListener('change', function() {
        // Verificar si al menos una opción está marcada
        var algunaOpcionMarcada = Array.from(opcionesTragos).some(function(opcion) {
            return opcion.checked;
        });

        // Mostrar u ocultar el botón según el estado de las opciones marcadas
        var botonSubmit = document.getElementById('botonSubmit');
        if (algunaOpcionMarcada) {
            botonSubmit.style.display = 'block'; // Mostrar el botón
        } else {
            botonSubmit.style.display = 'none'; // Ocultar el botón
        }
    });
});