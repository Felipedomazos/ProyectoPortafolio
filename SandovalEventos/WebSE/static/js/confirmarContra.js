function enableConfirmPassword() {
    var passwordInput = document.getElementById("password");
    var confirmPasswordInput = document.getElementById("confirm-password");
  
    if (passwordInput.value !== "") {
      confirmPasswordInput.disabled = false;
    } else {
      confirmPasswordInput.disabled = true;
    }
  }