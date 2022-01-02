  
//TODO: Make use of  django urls

function modificarUsuario(uvus) {
    window.location.href = '/admin/usuarios/modificar/'+uvus;
}

function eliminarUsuario(uvus) {
    window.location.href = '/admin/usuarios/eliminar/'+uvus;
}