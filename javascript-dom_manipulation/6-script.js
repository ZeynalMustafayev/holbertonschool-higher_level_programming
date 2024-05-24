function fetchData () {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
      if (!(response.ok)) {
        throw new Error('bayraa');
      }
      return response.json();
    })
    .then(data => {
      const name = document.getElementById('character');
      name.textContent = data.name;
    });
}
fetchData();
