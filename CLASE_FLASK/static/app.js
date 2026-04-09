const contenedor = document.getElementById("productos");
const contador = document.getElementById("contador");
const buscador = document.getElementById("buscador");

let productos = [];

// Cargar productos
async function cargarProductos() {
    const res = await fetch("/api/productos");
    productos = await res.json();
    mostrar(productos);
}

// Mostrar productos
function mostrar(lista) {
    contenedor.innerHTML = "";
    contador.innerText = `Total: ${lista.length}`;

    if (lista.length === 0) {
        contenedor.innerHTML = `
            <div class="sin-resultados">
                <h2>Sin resultados</h2>
                <p>No se encontró ningún producto</p>
            </div>
        `;
        return;
    }

    lista.forEach(p => {
        contenedor.innerHTML += `
        <div class="card">
            <h3>${p.nombre}</h3>
            <p>💲 ${p.precio}</p>
            <span>${p.categoria}</span>
            <button class="eliminar" onclick="eliminar(${p.id})">Eliminar</button>
        </div>`;
    });
}

// Agregar producto
document.getElementById("formulario").addEventListener("submit", async e => {
    e.preventDefault();

    const data = {
        nombre: document.getElementById("nombre").value,
        precio: document.getElementById("precio").value,
        categoria: document.getElementById("categoria").value
    };

    await fetch("/agregar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    cargarProductos();
    e.target.reset();
});

// Eliminar
async function eliminar(id) {
    await fetch(`/eliminar/${id}`, { method: "DELETE" });
    cargarProductos();
}

// Buscador
buscador.addEventListener("input", () => {
    const texto = buscador.value.toLowerCase();
    const filtrados = productos.filter(p =>
        p.nombre.toLowerCase().includes(texto)
    );
    mostrar(filtrados);
});

cargarProductos();