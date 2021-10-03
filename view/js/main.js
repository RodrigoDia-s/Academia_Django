function validar() {
    var usuario = document.getElementById('inputUsuario');
    var senha = document.getElementById('inputPassword');
    if(usuario.value == "" || senha.value == "") {
        
        usuario.style.borderColor = "red";
        senha.style.borderColor = "red";
        usuario.focus();
        senha.focus();
    }
}