
function eliminarProducto(id) {
    window.location.href = '/inventario/productos/eliminar/'+id;
}

function eliminarCategoria(id) {
    window.location.href = '/inventario/categoria/eliminar/'+id;
}

$(document).ready( function () {

    $('#tablaProductos').DataTable({
        responsive: true,
		"language" : {
			"url" : "https:////cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json"
		},
        "lengthMenu" : [ 5,4,3,2 ]
    });

    $('#tablaCategorias').DataTable({
        responsive: true,
		"language" : {
			"url" : "https:////cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json"
		},
        "lengthMenu" : [ 5,4,3,2 ],
    });

} );

function mostrarModalModificarProducto(id) {

    $.ajax({
        type: 'GET',
        url: '/inventario/modificarProducto/' + id,
        success: function (edit) {
            console.log("Hola")
            data = JSON.parse(edit)
            console.log(data["categoria"])
            $('#modalModificarProducto #id').val(id);
            $('#modalModificarProducto #nombreInput').val(data["nombre"]);
            $('#modalModificarProducto #categoriaInput').val(data["categoria"]);
            $('#modalModificarProducto #unidadesInput').val(data["unidades"]);
            $('#modalModificarProducto #valorMonetarioInput').val(data["valorMonetario"]);
            $('#modalModificarProducto #descripcionInput').val(data["descripcion"]);

        }
    });

}