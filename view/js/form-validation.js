// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

       
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })

  })()


  function validateMyForm2() {
    var registrogeral = document.getElementById('rg')
    alert("registrogeral")
    if(isNaN(registrogeral.value) )
    {
        alert("Somente números no campo telefone")
        registrogeral.focus();
        return false;
    }

    alert("Enviado");
    return true;
}

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

function VerificarSenha() {
  var senha = document.getElementById('senha1').value
  var senha2 = document.getElementById('senha2').value

  if(senha != senha2) {
    alert("Senhas diferentes")
    return false
  }
  

    alert("Cadastrado")
   let a = document.createElement('a');
    a.target = '_blank';
    a.href = '/view/AreaAluno.html';
    a.click();
    window.close()
    return true
   
}

function VerificarSenha2() {
  var senha3 = document.getElementById('senha3').value
  var senha4 = document.getElementById('senha4').value

  if(senha3 != senha4) {
    alert("Senhas diferentes")
    return false
  }
  

    alert("Cadastrado")
   let a = document.createElement('a');
    a.target = '_blank';
    a.href = '/view/AreaAluno.html';
    a.click();
    window.close()
    return true
   
}


