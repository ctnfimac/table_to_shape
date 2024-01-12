window.onload = function () {
    const conexionForm = document.getElementById('conexionForm')
    const conexionMensaje = document.getElementById('conexionMensaje')
    const btnDescargar = document.getElementById('btnDescargar')
    const btnImgDescargar = document.getElementById('btnImgDescargar')
    const msj = document.getElementById('msj')

    conexionMensaje.style.display = 'none';

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
            if(data.errors){
                msj.innerHTML= '<strong>Credenciales incorrectas</strong>'
                conexionMensaje.style.display = 'block';
                conexionMensaje.classList.remove('alert-success');
                conexionMensaje.classList.remove('alert-danger');
                conexionMensaje.classList.add('alert-warning');
                btnDescargar.classList.add('disabled');
                btnImgDescargar.style.cursor = 'unset';
                btnImgDescargar.style.opacity = '0.2';               
            }else{
                msj.innerHTML= '<strong>Conexión establecida</strong>'
                conexionMensaje.style.display = 'block';
                conexionMensaje.classList.remove('alert-warning');
                conexionMensaje.classList.remove('alert-danger');
                conexionMensaje.classList.add('alert-success');
                btnDescargar.classList.remove('disabled');
                btnImgDescargar.style.cursor = 'pointer';
                btnImgDescargar.style.opacity = '1';
            }
        })
        .catch( error => {
            msj.innerHTML= '<strong>Error en el sistema</strong>'
            conexionMensaje.style.display = 'block';
            conexionMensaje.classList.remove('alert-success');
            conexionMensaje.classList.remove('alert-warning');
            conexionMensaje.classList.add('alert-danger');
            btnDescargar.classList.add('disabled');
            btnImgDescargar.style.cursor = 'unset';
            btnImgDescargar.style.opacity = '0.2';
        })
        

    })

    const closeBtn = document.querySelector('.close');
    closeBtn.addEventListener('click', () => {
        conexionMensaje.style.display = 'none';
    });
}
