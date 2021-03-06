import fetch from 'node-fetch';

export async function obtenerPeliculas(){
    const response = await fetch("http://127.0.0.1:5000/kodi/pelis")
    /*
    const response = await fetch('http://127.0.0.1:5000/kodi/pelis', {
        method: 'POST',
        //mode: 'cors',
        //cache: 'default',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'datos': 'pelis'}) });
      
        //const response = await fetch('http://127.0.0.1:5000/');
        //const body = await response.text();
        */
    const body = await response.json()
    return body['result']['movies'];
}

export async function obtenerPeliculasFiltro(filtro, valor){
    //const response = await fetch("http://127.0.0.1:5000/kodi/pelis/"+filtro+"_"+valor)
    const response = await fetch('http://127.0.0.1:5000/kodi/pelis/filtro', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'tipo': filtro, 'dato': valor}) });
    const body = await response.json()
    return body['result']['movies'];
}

export async function obtenerPeliculasInfo(idPeli){
    const response = await fetch("http://127.0.0.1:5000/kodi/pelidetalles/"+idPeli)

    const body = await response.json()
    return body['result']['moviedetails'];
  
}

export async function obtenerSeries(){
    const response = await fetch("http://127.0.0.1:5000/kodi/series")

    const body = await response.json()
    return body['result']['tvshows'];
  
}

export async function obtenerSeriesInfo(idSerie){
    const response = await fetch("http://127.0.0.1:5000/kodi/seriedetalles/"+idSerie)

    const body = await response.json()
    return body['result']['tvshowdetails'];
}

export async function reproducirPeli(idPeli){
    await fetch("http://127.0.0.1:5000/kodi/play/peli/"+idPeli)
}
