function toggleForm(formType) {
    if (formType === 'login') {
        document.getElementById("loginForm").style.display = "block";
        document.getElementById("cadastroForm").style.display = "none";
        document.getElementById("formTitle").innerText = "Login";
        document.getElementById("switchToLogin").style.display = "none";
        document.getElementById("switchToCadastro").style.display = "block";
    } else {
        document.getElementById("loginForm").style.display = "none";
        document.getElementById("cadastroForm").style.display = "block";
        document.getElementById("formTitle").innerText = "Cadastro";
        document.getElementById("switchToLogin").style.display = "block";
        document.getElementById("switchToCadastro").style.display = "none";
    }
}

toggleForm('cadastro');