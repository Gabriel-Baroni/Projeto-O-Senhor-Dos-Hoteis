function toggleForm(formType) {
    const loginForm = document.getElementById('loginForm');
    const cadastroForm = document.getElementById('cadastroForm');
    const switchToCadastro = document.getElementById('switchToCadastro');
    const switchToLogin = document.getElementById('switchToLogin');
    const rightSection = document.querySelector('.right-section');
    const leftSection = document.querySelector('.left-section');
    const formTitle = document.getElementById('formTitle');

    if (formType === 'login') {
        // Ativando o formulário de login
        loginForm.classList.add('active');
        cadastroForm.classList.remove('active');
        formTitle.textContent = 'Login';

        // Alterna visibilidade dos botões
        switchToCadastro.style.display = 'inline-block';
        switchToLogin.style.display = 'none';

        // Movendo as seções
        rightSection.classList.add('move-left');
        rightSection.classList.remove('move-right');
        leftSection.classList.add('move-right');
        leftSection.classList.remove('move-left');
    } else if (formType === 'cadastro') {
        // Ativando o formulário de cadastro
        cadastroForm.classList.add('active');
        loginForm.classList.remove('active');
        formTitle.textContent = 'Cadastro';

        // Alterna visibilidade dos botões
        switchToCadastro.style.display = 'none';
        switchToLogin.style.display = 'inline-block';

        // Movendo as seções
        rightSection.classList.add('move-right');
        rightSection.classList.remove('move-left');
        leftSection.classList.add('move-left');
        leftSection.classList.remove('move-right');
    }
}

// Inicializa a exibição do formulário
window.onload = function () {
    document.getElementById('cadastroForm').classList.add('active');
};
