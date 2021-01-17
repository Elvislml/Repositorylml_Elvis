$(document).ready(function () {

    obtenerTareas();
    
    function obtenerTareas(){
        $.ajax({
            url: 'listar.php',
            type: "GET",
            success: function(tareas){
                let listPersona = JSON.parse(tareas);
                let template = '';
                listPersona.forEach(persona =>{
                    template += `
                    <tr taskId="${persona.id}">
                        <td>${persona.id}</td>
                        <td>${persona.nombre}</td>
                        <td>${persona.apellido}</td>
                        <td>
                            <button class="task-modify btn btn-primary">
                                Editar
                            </button>
                        </td>
                        <td>
                            <button class="task-delete btn btn-danger">
                                Eliminar
                            </button>
                        </td>
                    </tr>
                    `
                });
                $('#listPersona').html(template);
            }
        });
    }


    $("#funciones").dialog({
		autoOpen:false,
        width:500
	});
	
	$('#agregar').click(function(){
		$('#funciones').attr('title', 'Agregar');
		$('#action').val('insert');
		$('#form_action').val('Insert');
		$('#formUser')[0].reset();
		$('#form_action').attr('disabled', false);
		$("#funciones").dialog('open');
	});
	
	$('#formUser').on('submit', function(event){
		event.preventDefault();
		var error_nombre = '';
		var error_apellido = '';
		if($('#nombre').val() == '')
		{
			error_nombre = 'Se requiere el Nombre';
			$('#errorNombre').text(error_nombre);
			$('#nombre').css('border-color', '#cc0000');
		}
		else
		{
			error_nombre = '';
			$('#errorNombre').text(error_nombre);
			$('#nombre').css('border-color', '');
		}
		if($('#apellido').val() == '')
		{
			error_apellido = 'Se requiere el Apellido';
			$('#errorApellido').text(error_apellido);
			$('#apellido').css('border-color', '#cc0000');
		}
		else
		{
			error_apellido = '';
			$('#errorApellido').text(error_apellido);
			$('#apellido').css('border-color', '');
		}
		
		if(error_nombre != '' || error_apellido != '')
		{
			return false;
		}
		else
		{
			$('#form_action').attr('disabled', 'disabled');
			var form_data = $(this).serialize();
			$.ajax({
				url:"insertar.php",
				method:"POST",
				data:form_data,
				success:function(data)
				{
					$('#funciones').dialog('close');
					$('#action_alert').html(data);
					$('#action_alert').dialog('open');
					obtenerTareas();
					$('#form_action').attr('disabled', false);
				}
			});
		}
		
    });

    $('#action_alert').dialog({
		autoOpen:false
    });

    $(document).on('click', '.task-modify', (e)=>{
        const elemento = $(this)[0].activeElement.parentElement.parentElement;
        const id = $(elemento).attr('taskId');
        console.log(id);
        $.post('getSeleccion.php',{id},(response)=>{
            console.log(response);
            const persona = JSON.parse(response);
		    $('#nombre').val(persona.nombre);
		    $('#apellido').val(persona.apellido);
			$('#funciones').attr('title', 'Edit Data');
			$('#action').val('update');
			$('#hidden_id').val(persona.id);
			$('#form_action').val('Update');
            $('#funciones').dialog('open');
        });
	});


    $(document).on('click', '.task-delete', (e)=>{
		if(confirm('Desea eliminar el registros')){
			const elemento = $(this)[0].activeElement.parentElement.parentElement;
			const id = $(elemento).attr('taskId');
			$.post('eliminar.php',{id},(response)=>{
				obtenerTareas();
			});
		}
    });

});