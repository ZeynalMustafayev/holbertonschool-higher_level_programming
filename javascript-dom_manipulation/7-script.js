function fetchMovie () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!(response.ok)) {
        throw new Error('bayraa');
      }
      return response.json();
    })
    .then(data => {
      const listMovie = document.getElementById('list_movies');
      data.results.forEach(film => {
        const newElement = document.createElement('li');
        newElement.textContent = film.title;
        listMovie.append(newElement);
      });
    })
    .catch(Error('bayraa'));
}
fetchMovie();
