const form = document.getElementById('signupForm');
const errorDiv = document.getElementById('error');

form.addEventListener('submit', function(event) {
  const username = form.username.value.trim();
  const email = form.email.value.trim();
  const pass1 = form.password1.value.trim();
  const pass2 = form.password2.value.trim();

  if (!username || !email || !pass1 || !pass2 || pass1 !== pass2) {
    event.preventDefault();
    errorDiv.style.display = 'block';
  } else {
    errorDiv.style.display = 'none';
  }
});