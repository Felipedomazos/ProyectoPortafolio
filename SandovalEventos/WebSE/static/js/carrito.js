function openNav() {
    document.getElementById("SidenavCarrito").style.width = "100%";
    document.getElementById("SidenavCarrito").style.left = "0"; // Agrega esta línea
  }
  
  function closeNav() {
    document.getElementById("SidenavCarrito").style.width = "0";
  }

function agregarAlCarrito(idProducto) {
    // Obtener el elemento del producto seleccionado
    var producto = document.getElementById(idProducto);


    // Obtener los detalles del producto
    var imagen = producto.querySelector('img').src;
    var nombre = producto.querySelector('h3').textContent;
    var precio = producto.querySelector('.price').textContent;


    // Crear un nuevo elemento para el producto en el sidenav
    var nuevoProducto = document.createElement('div');
    nuevoProducto.classList.add('producto-carrito');
    nuevoProducto.innerHTML = `
      <div class="contador">
        <button class="contador-btn" onclick="incrementarContador(this)">+</button>
        <span class="contador-valor">1</span>
        <button class="contador-btn" onclick="decrementarContador(this)">-</button>
      </div>
      <img src="${imagen}" alt="${nombre}" />
      <div class="info">
        <h4>${nombre}</h4>
        <p>Precio: ${precio}</p>
      </div>
      <button class="eliminar-producto" onclick="eliminarDelCarrito(this)">Eliminar</button>
    `;


    // Agregar el nuevo producto al sidenav
    var listaProductos = document.getElementById('listaProductos');
    listaProductos.appendChild(nuevoProducto);

    var x = document.getElementById("msj");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3500);
}


function eliminarDelCarrito(botonEliminar) {
    // Obtener el elemento padre del botón (producto-carrito)
    var producto = botonEliminar.parentNode;


    // Eliminar el producto del DOM
    producto.parentNode.removeChild(producto);
}


function decrementarContador(botonContador) {
    var contadorValor = botonContador.previousElementSibling;
    var valor = parseInt(contadorValor.textContent);
    if (valor > 1) {
        contadorValor.textContent = valor - 1;
    }
}


function incrementarContador(botonContador) {
    var contadorValor = botonContador.nextElementSibling;
    var valor = parseInt(contadorValor.textContent);
    contadorValor.textContent = valor + 1;
}