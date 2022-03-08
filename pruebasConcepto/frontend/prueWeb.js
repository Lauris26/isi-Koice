import fetch from 'node-fetch';

/*
fetch('http://127.0.0.1:5000/kodi/pelis')
  .then(response => response.json())
  .then(data => console.log(data));
*/

function convertToDataURLviaCanvas(url, callback, outputFormat){
  var img = new Image();
  img.crossOrigin = 'Anonymous';
  img.onload = function(){
      var canvas = document.createElement('CANVAS');
      var ctx = canvas.getContext('2d');
      var dataURL;
      canvas.height = this.height;
      canvas.width = this.width;
      ctx.drawImage(this, 0, 0);
      dataURL = canvas.toDataURL(outputFormat);
      callback(dataURL);
      canvas = null; 
  };
  img.src = url;
}

async function obtenerLibrary(){
  const response = await fetch('http://127.0.0.1:5000/');
  const body = await response.text();

  console.log(body);
  //const body = await response.text();
  //var jsonData = JSON.parse(body);
  return body['result'];
}

async function obtenerPelis() {
  const response = await fetch('http://127.0.0.1:5000/kodi/pelis');
  const body = await response.text();

  console.log(body);
  var jsonData = JSON.parse(body);

  var token = jsonData['id'];

  var pelis = jsonData['result']['movies'];

  console.log(jsonData);

  console.log(token);

  console.log(pelis);
  var idPeli = pelis[0]['movieid'];
  return idPeli;
}

async function reproducirPeliId(idPeli) {
  var response1 = await fetch('http://127.0.0.1:5000/kodi/pelis/' + idPeli);
  var body1 = await response1.text();
  console.log(body1);
}

console.log("inicio");

obtenerLibrary();
//console.log(obtenerLibrary());

//var idPeli = await obtenerPelis();

//await reproducirPeliId(idPeli);

console.log("fin");




