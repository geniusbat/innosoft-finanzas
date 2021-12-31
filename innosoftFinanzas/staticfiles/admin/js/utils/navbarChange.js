$(document).ready( function () {
    nombreNav = document.getElementById("navbar").className
    listaNombres = ["home","admin","necesidades","sugerencias","login","register"];
    listaNombres.pop(nombreNav)
    listaNombres.forEach(function(elemento, indice, array) {
        document.getElementById(elemento).className = "nav-link";
})
    document.getElementById(nombreNav).className = "nav-link active";
})