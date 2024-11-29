function toggleForm(formType) {
    const loginForm = document.getElementById('loginForm');
    const cadastroForm = document.getElementById('cadastroForm');
    const switchToCadastro = document.getElementById('switchToCadastro');
    const switchToLogin = document.getElementById('switchToLogin');
    
    if (formType === 'login') {
        loginForm.classList.add('active');
        cadastroForm.classList.remove('active');
        switchToCadastro.style.display = 'inline-block';
        switchToLogin.style.display = 'none';
    } else if (formType === 'cadastro') {
        cadastroForm.classList.add('active');
        loginForm.classList.remove('active');
        switchToCadastro.style.display = 'none';
        switchToLogin.style.display = 'inline-block';
    }
}

// Inicializa a exibição do formulário
window.onload = function() {
    document.getElementById('cadastroForm').classList.add('active');
};