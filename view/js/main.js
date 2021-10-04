function validateMyForm() {

    var user = document.getElementById("inputUsuario");
    var pass = document.getElementById("inputPassword");


    if (user.value == "" || pass.value == "") {
        if (user.value == "") {
            alert("Preencha o usuário")
            user.style.borderColor = 'red';
            user.focus();

            return false;
        }
        else {
            alert("Preencha a senha")
            pass.style.borderColor = 'red';
            pass.focus();
            return false;
        }
    }

    let a = document.createElement('a');
    a.target = '_blank';
    a.href = '/view/default.html';
    a.click();
    alert("Logado");
    return true;


}