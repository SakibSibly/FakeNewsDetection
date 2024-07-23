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
    } 
    
    else if (Pass.value == "") {
        passwordErrorMessage.style.display = 'block'; 
        passwordErrorMessage.textContent = 'Please provide your password!';
        passParent.classList.add('error-input-container'); 
        return false;
    } 
    
    else {
       
        return true;
    }
}

// Eye Btn
function toggleEyeButton() {
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


// register error message

document.addEventListener('DOMContentLoaded', function() {

    const form = document.getElementById('registration-form');

    form.addEventListener('submit', function(event) {
       
        let isFormValid = true;

        
        isFormValid &= validateField('name', 'error-message-name', '.fa-user');
        isFormValid &= validateField('user-name', 'error-message-username', '.fa-user'); 
        isFormValid &= validateField('mail', 'error-message-email', '.fa-envelope'); 
        isFormValid &= validateField('pass', 'error-message-password', '.fa-lock'); 
        isFormValid &= validateField('pass', 'error-message-password', '.fa-eye'); 
        isFormValid &= validateField('pass', 'error-message-password', '.fa-eye-slash');

       
        if (!isFormValid) {
            event.preventDefault();
        }

        
    });
});

function validateField(inputId, errorId, iconClass) {
    const input = document.getElementById(inputId);
    const error = document.getElementById(errorId);
    const inputField = input.closest('.input-field');
    const icon = inputField.querySelector(iconClass);

    if (input.value.trim() === '') { 

        error.classList.remove('hidden');
        inputField.classList.add('error-border');
        if (icon) icon.classList.add('error-icon');

        return false; 
    } 
    
    
    else {
        error.classList.add('hidden');
        inputField.classList.remove('error-border');

        if (icon) icon.classList.remove('error-icon');

        return true; 
    }
}