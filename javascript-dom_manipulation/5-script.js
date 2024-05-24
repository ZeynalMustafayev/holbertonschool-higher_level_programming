const updateHeader = document.getElementById('update_header');
const newText = document.querySelector('header');

updateHeader.addEventListener('click', function () {
  newText.textContent = 'New Header!!!';
});
