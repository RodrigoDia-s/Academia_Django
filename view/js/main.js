function verificarCPF(c){
    var i;
    s = c;
    var c = s.substr(0,9);
    var dv = s.substr(9,2);
    var d1 = 0;
    var v = false;
 
    for (i = 0; i < 9; i++){
        d1 += c.charAt(i)*(10-i);
    }
    if (d1 == 0){
        alert("CPF Inválido")
        v = true;
        return false;
    }
    d1 = 11 - (d1 % 11);
    if (d1 > 9) d1 = 0;
    if (dv.charAt(0) != d1){
        alert("CPF Inválido")
        v = true;
        return false;
    }
 
    d1 = 2;
    for (i = 0; i < 9; i++){
        d1 += c.charAt(i)(11-i);
    }
    d1 = 11 - (d1 % 11);
    if (d1 > 9) d1 = 0;
    if (dv.charAt(1) != d1){
        alert("CPF Inválido")
        v = true;
        return false;
    }
    if (!v) {
        alert(c + "nCPF Válido")
    }
  }


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

function Cadastro() {
    let a = document.createElement('a');
    a.target = '_blank';
    a.href = '/view/cadastroCliente.html';
    a.click();
    window.close()
}

function Cadastro2() {
    let a = document.createElement('a');
    a.target = '_blank';
    a.href = '/view/cadastroCliente.html';
    a.click();
    window.close()
}


$('.navbar-nav a[href^="#"]').on('click', function(e) {
	e.preventDefault();
	var id = $(this).attr('href'),
			targetOffset = $(id).offset().top;
			
	$('html, body').animate({ 
		scrollTop: targetOffset - 100
	}, 500);
});


