
    setTimeout(() => {
      document.querySelectorAll('.flash-message').forEach(msg => {
        msg.style.transition = "opacity 0.5s ease";
        msg.style.opacity = 0; 
        setTimeout(() => msg.remove(), 500);
      });
    }, 5000); 