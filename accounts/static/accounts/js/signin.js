function signinn() {
    var Mail = document.getElementById('mail');
    var Pass = document.getElementById('pass');
    var emailErrorMessage = document.getElementById('email-error-message');
    var passwordErrorMessage = document.getElementById('password-error-message');

    var mailParent = Mail.closest('.input-field');
    var passParent = Pass.closest('.input-field');

    emailErrorMessage.style.display = 'none';
    mailParent.classList.remove('error-input-container');
    passwordErrorMessage.style.display = 'none';
    passParent.classList.remove('error-input-container');

    if (Mail.value == "") {
        emailErrorMessage.style.display = 'block'; 
        emailErrorMessage.textContent = 'Please provide your email!';
        mailParent.classList.add('error-input-container'); 
        return false;
    } else if (Pass.value == "") {
        passwordErrorMessage.style.display = 'block'; 
        passwordErrorMessage.textContent = 'Please provide your password!';
        passParent.classList.add('error-input-container'); 
        return false;
    } else {
       
        return true;
    }
}

// Eye Btn
function pass() {
    var passInput = document.getElementById('pass');
    var passIcon = document.getElementById('pass-icon');

    if (passInput.type === "password") {
        passInput.type = "text";
        passIcon.className = "fa-solid fa-eye-slash";
    } else {
        passInput.type = "password";
        passIcon.className = "fa-solid fa-eye";
    }
}

document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    let isValid = true; 

    
    function validateField(inputId, errorId) {
        const input = document.getElementById(inputId);
        const error = document.getElementById(errorId);
        if (input.value.trim() === '') {
            error.classList.remove('hidden');
            isValid = false;
        } else {
            error.classList.add('hidden');
        }
    }


    validateField('name', 'error-message-name'); 
    validateField('user-name', 'error-message-username');
    validateField('mail', 'error-message-email');
    validateField('pass', 'error-message-password');

    
    if (isValid) {
        document.getElementById('registration-form').submit();
    }
});