$(document).ready(function(){
    
    obtenerTareas();

    function obtenerTareas(){
        $.ajax({
            url: 'listar.php',
            type: "GET",
            success: function(tareas){
                let tasks = JSON.parse(tareas);
                let template = '';
                tasks.forEach(task =>{
                    template += `
                    <tr taskId="${task.id}">
                        <td>${task.id}</td>
                        <td>
                            <a href="#" class="task-item" title="Pulsar para editar">${task.name}</a>
                        </td>
                        <td>${task.description}</td>
                        <td>
                            <button class="task-delete btn btn-danger">
                                Eliminar
                            </button>
                        </td>
                    </tr>
                    `
                });
                $('#tasks').html(template);
            }
        });
    }

    $('#task-form').submit(e=>{
        const datos = {
            name: $('#name').val(),
            description: $('#description').val(),
            id: $('#id').val(),
        }
        const url = modificar === false ? 'insertar.php': 'modificar.php';
        $.post(url, datos, (response) =>{
            obtenerTareas();
        });
    });

    $(document).on('click','.task-item',(e)=>{
        const elemento = $(this)[0].activeElement.parentElement.parentElement;
        const id = $(elemento).attr('taskId');
        console.log(id);

        $.post('getTareas.php',{id},(response) =>{
            console.log(response);
            const task = JSON.parse(response);
            $('#name').val(task.name);
            $('#description').val(task.description);
            $('#id').val(task.id);
            modificar=true;
        });
    });

});
