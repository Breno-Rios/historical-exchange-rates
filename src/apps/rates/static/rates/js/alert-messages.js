    

    function showMessage(message, type = 'warning') {
        const formMessage = document.getElementById('error-message');
        if (!formMessage) return;

        formMessage.classList.remove("alert-danger", "alert-warning");
        formMessage.classList.add("alert", `alert-${type}`);
    
        formMessage.textContent = message;
        formMessage.style.display = "block"; // mostra o alert
    }

    function hideMessage() {
        const formMessage = document.getElementById('error-message');
        if (!formMessage) return;
        
        formMessage.textContent = "";
        formMessage.style.display = "none"; // esconde o alert
    }