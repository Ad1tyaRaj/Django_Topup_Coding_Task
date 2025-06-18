const form = document.getElementById('loginForm');
const errorDiv = document.getElementById('error');

form.addEventListener('submit', function(event) {
  const username = form.username.value.trim();
  const password = form.password.value.trim();

  if (!username || !password) {
    event.preventDefault();
    errorDiv.style.display = 'block';
  } else {
    errorDiv.style.display = 'none';
  }
});