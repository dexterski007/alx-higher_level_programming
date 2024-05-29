$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      response.results.forEach(function (movie) {
        $('UL#list_movies').append('<li>' + (movie.title) + '</li>');
      });
    }
  });
});
