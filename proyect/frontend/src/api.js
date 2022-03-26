import fetch from 'node-fetch';

export async function obtenerPeliculas(){
    const response = await fetch("http://127.0.0.1:5000/kodi/pelis")
    const body = await response.json()
    return body['result']['movies'];
  
}

export async function obtenerSeries(){
    const response = await fetch("http://127.0.0.1:5000/kodi/series")
    const body = await response.json()
    return body['result']['tvshows'];
  
}