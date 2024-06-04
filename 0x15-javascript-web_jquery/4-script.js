var header = document.getElementsByTagName('header')[0];

var toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function() {
	if (header.className === 'red') {
		header.className = 'green';
	} else {
		header.className = 'red';
	}
});
