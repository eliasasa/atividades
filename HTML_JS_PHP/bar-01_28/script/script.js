document.getElementById("menu-toggle").addEventListener("click", dropdown);

function dropdown(event) {
    const navMenu = document.getElementById("nav-menu");
    navMenu.classList.toggle("visible");
}

