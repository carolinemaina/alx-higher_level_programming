$.ajax({
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	method: 'GET',
	success: function(data) {
		var movies = data.results;
		var ul = $('<ul id="list_movies"></ul>');

		$.each(movies, function(index, movie) {
			ul.append('<li>' + movie.title + '</li>');
		});

		$('body').append(ul);
	}
});
