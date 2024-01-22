window.onload = function () {
    const conexionForm = document.getElementById('conexionForm')
    const conexionMensaje = document.getElementById('conexionMensaje')
    const btnDescargar = document.getElementById('btnDescargar')
    const imgDescargar = document.getElementById('imgDescargar')
    const msj = document.getElementById('msj')
    
    conexionMensaje.style.display = 'none';
    
    // inputs del formulario para elegir esquema y tablas
    const schema = document.getElementById('schema')
    const tablesdb = document.getElementById('tablesdb')


    conexionForm.addEventListener('submit', (event) => {
        event.preventDefault()

        fetch(conexionForm.action,{
            method: 'POST',
            body: new FormData(conexionForm),
            headers:{
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': conexionForm.elements.csrfmiddlewaretoken.value,
            }
        })
        .then( response => response.json())
        .then( data => {
            clean_select_schemas()  
            clean_select_tables()  
            if(data.errors){
                msj.innerHTML= '<strong>Credenciales incorrectas</strong>'
                conexionMensaje.style.display = 'block';
                conexionMensaje.classList.remove('alert-success');
                conexionMensaje.classList.remove('alert-danger');
                conexionMensaje.classList.add('alert-warning');
                btnDescargar.classList.add('disabled');
                imgDescargar.style.cursor = 'unset';
                imgDescargar.style.opacity = '0.3';           
            }else{
                msj.innerHTML= '<strong>Conexión establecida</strong>'
                conexionMensaje.style.display = 'block';
                conexionMensaje.classList.remove('alert-warning');
                conexionMensaje.classList.remove('alert-danger');
                conexionMensaje.classList.add('alert-success');
                btnDescargar.classList.remove('disabled');
                imgDescargar.style.cursor = 'pointer';
                imgDescargar.style.opacity = '1';
                build_schema(data.schemas)
                build_tables(data.tables)
            }
        })
        .catch( error => {
            msj.innerHTML= '<strong>Error en el sistema</strong>'
            conexionMensaje.style.display = 'block';
            conexionMensaje.classList.remove('alert-success');
            conexionMensaje.classList.remove('alert-warning');
            conexionMensaje.classList.add('alert-danger');
            btnDescargar.classList.add('disabled');
            imgDescargar.style.cursor = 'unset';
            imgDescargar.style.opacity = '0.3';
        })
    })


    schema.addEventListener('change', (event) => {
        clean_select_tables()
        data = { schema: schema.value}

        fetch('/web/tables/' + schema.value,{
            method: 'GET',
            headers:{
                "Content-Type": "application/json",
                'X-Requested-With': 'XMLHttpRequest',
            }
        })
        .then( response => response.json())
        .then( data => {
            if(data.errors){
                console.error(data)
            }else{
                build_tables(data.tables)
            }
        })
        .catch( error => {
            console.error(error)
        })
    })

    // boton para cerrar el mensaje de conexion mediante
    // el formulario
    const closeBtn = document.querySelector('.close');
    closeBtn.addEventListener('click', () => {
        conexionMensaje.style.display = 'none';
    });


    function build_schema(schemas){
        schemas.forEach(element => {
            var opt = document.createElement('option');
            opt.value = element;
            opt.innerHTML = element;
            schema.appendChild(opt);
        });
    }

    function build_tables(tables){
        tables.forEach(element => {
            var opt = document.createElement('option');
            opt.value = element;
            opt.innerHTML = element;
            tablesdb.appendChild(opt);
        });
    }

    function clean_select_schemas(){
        var length = schema.options.length;
        for (i = length-1; i >= 0; i--) {
            schema.options[i] = null;
        }
    }

    function clean_select_tables(){
        var length = tablesdb.options.length;
        for (i = length-1; i >= 0; i--) {
            tablesdb.options[i] = null;
        }
    }
}
