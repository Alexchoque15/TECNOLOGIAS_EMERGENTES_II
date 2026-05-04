console.log("Web cargada");

// ANIMACIÓN DE ENTRADA
const cards = document.querySelectorAll(".card");

const mostrarCards = () => {
    cards.forEach(card => {
        const pos = card.getBoundingClientRect().top;

        if (pos < window.innerHeight - 50) {
            card.classList.add("opacity-100", "translate-y-0");
        }
    });
};

window.addEventListener("scroll", mostrarCards);
window.addEventListener("load", mostrarCards);

window.addEventListener("scroll", () => {
    const navbar = document.getElementById("navbar");

    if (window.scrollY > 50) {
        navbar.classList.add("bg-white", "shadow");
    } else {
        navbar.classList.remove("bg-white", "shadow");
    }
});