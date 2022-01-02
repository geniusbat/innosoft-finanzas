
function modificarNecesidad(id) {
    window.location.href = '/necesidades/modificar/'+id;
}

function eliminarNecesidad(id) {
    window.location.href = '/necesidades/eliminar/'+id;
}

function eliminarComite(id) {
    window.location.href = '/necesidades/comite/eliminar/'+id;
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

function mostrarModalModificarNecesidad(id) {

    $.ajax({
        type: 'GET',
        url: '/necesidades/modificar/' + id,
        success: function (edit) {
            data = JSON.parse(edit)
            console.log($('#modalModificarNecesidad #comiteInput').val)
            $('#modalModificarNecesidad #id').val(id);
            $('#modalModificarNecesidad #nombreInput').val(data["nombre"]);
            $('#modalModificarNecesidad #comiteInput').val(data["comite"]);
            $('#modalModificarNecesidad #cantidadInput').val(data["cantidad"]);
            $('#modalModificarNecesidad #descripcionInput').val(data["descripcion"]);
        }
    });

}