setTimeout(() => {
  document.querySelectorAll('.flash-message').forEach(msg => {
    // Inicia a transição de opacidade
    msg.style.transition = "opacity 0.5s ease";
    msg.style.opacity = 0; 

    // Após 500ms (tempo da transição), remove o elemento
    setTimeout(() => {
      msg.remove();
    }, 500); // Tempo para a transição de opacidade
  });
}, 5000); // 5000ms = 5 segundos
