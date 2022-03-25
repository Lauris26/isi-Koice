import fetch from 'node-fetch';

/*
const pelis={
  peliculas:[
         {
           id: 1,
           poster: "https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg",
           titulo: "vengadores"
         },
         {
           id:2,
           poster: "https://m.media-amazon.com/images/M/MV5BNGZiMzBkZjMtNjE3Mi00MWNlLWIyYjItYTk3MjY0Yjg5ODZkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SX300.jpg",
           titulo: "vengadores 2"
         },
         {
           id:3,
           poster: "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
           titulo: "vengadores 3"
         }
       ]
      }*/
/*
async function obtenerLibrary(){
  const response = await fetch('http://127.0.0.1:5000/');
  const body = await response.text();

  console.log(body);
  //const body = await response.text();
  //var jsonData = JSON.parse(body);
  return body['result'];
}*/

export function obtenerPelis() {
  const response = await fetch('http://127.0.0.1:5000/kodi/pelis');
  const body = await response.text();

  //console.log(body);
  var jsonData = JSON.parse(body);

  //var token = jsonData['id'];

  var pelis = jsonData['result']['movies'];

  //console.log(jsonData);

  //console.log(token);

  //console.log(pelis);
  //var idPeli = pelis[0]['movieid'];
  return pelis;
}

export async function obtenerSeries() {
  const response = await fetch('http://127.0.0.1:5000/kodi/series');
  const body = await response.text();

  console.log(body);
  var jsonData = JSON.parse(body);

  var token = jsonData['id'];

  var pelis = jsonData['result']['tvshows'];

  console.log(jsonData);

  console.log(token);

  console.log(pelis);
  var idPeli = pelis[0]['tvshowid'];
  return idPeli;
}

export async function reproducirPeliId(idPeli) {
  var response1 = await fetch('http://127.0.0.1:5000/kodi/pelis/' + idPeli);
  var body1 = await response1.text();
  console.log(body1);
}

/*
console.log("inicio");

console.log(obtenerLibrary());

console.log("fin");
*/



