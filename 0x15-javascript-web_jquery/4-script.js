const header = document.getElementsByTagName('header')[0];

const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
  if (header.className === 'red') {
    header.className = 'green';
  } else {
    header.className = 'red';
  }
});
