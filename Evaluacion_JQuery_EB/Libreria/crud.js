$(document).ready(function () {
	let modificar = false;

    obtenerTareas();
    
    function obtenerTareas(){
        $.ajax({
            url: 'listar.php',
            type: "GET",
            success: function(tareas){
                let listAlumnos = JSON.parse(tareas);
                let template = '';
                listAlumnos.forEach(persona =>{
                    template += `
					<tr taskId="${persona.id}">
                        <td>${persona.codigo}</td>
						<td>${persona.nombres}</td>
						<td>${persona.telefono}</td>
                        <td>${persona.direccion}</td>
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
                $('#listAlumnos').html(template);
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
		$('#form_action').attr('disabled', 'disabled');
		var form_data = $(this).serialize();
		$.ajax({
			url:"insertar.php",
			method:"POST",
			data:form_data,
			success:function(data){
				$('#funciones').dialog('close');
				$('#action_alert').html(data);
				$('#action_alert').dialog('open');
				obtenerTareas();
				$('#form_action').attr('disabled', false);
			}
		});
	});

    $('#action_alert').dialog({
		autoOpen:false
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

	$(document).on('click', '.task-modify', function () {
		let elemento = $(this)[0].parentElement.parentElement;
		let id = $(elemento).attr('taskId');
		console.log(id);
		$.post('getSeleccion.php',{id},(response)=>{
            console.log(response);
			const persona = JSON.parse(response);
			$('#codigo').val(persona.codigo);
		    $('#nombres').val(persona.nombres);
			$('#telefono').val(persona.telefono);
			$('#direccion').val(persona.direccion);
			$('#funciones').attr('title', 'Edit Data');
			$('#action').val('update');
			$('#hidden_id').val(persona.id);
			$('#form_action').val('Update');
            $('#funciones').dialog('open');
        });
	});


	
    $('#search').keyup(function(){
		if($('#search').val()){
			let search = $('#search').val();
			$.ajax({
				url: 'buscar.php',
				type: 'POST',
				data: {search},
				success: function(response){
					let tasks = JSON.parse(response);
					let template = '';
					tasks.forEach(persona =>{
						template += `
						<tr taskId="${persona.id}">
							<td>${persona.codigo}</td>
							<td>${persona.nombres}</td>
							<td>${persona.telefono}</td>
							<td>${persona.direccion}</td>
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
						`;
					});
					$('#listAlumnos').html(template);
				}
			});
		}else{
			obtenerTareas();
		}
	});
});