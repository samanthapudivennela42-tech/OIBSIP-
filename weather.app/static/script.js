async function getWeather(){

const city=document.getElementById("city").value;

if(city.trim()==""){

alert("Enter City Name");

return;

}

const response=await fetch(`/weather?city=${city}`);

const data=await response.json();

const result=document.getElementById("result");

if(data.error){

result.innerHTML=`<h3>${data.error}</h3>`;

return;

}

result.innerHTML=`

<h2>${data.city}, ${data.country}</h2>

<img src="https://openweathermap.org/img/wn/${data.icon}@2x.png">

<p><b>Temperature:</b> ${data.temperature_c} °C</p>

<p><b>Temperature:</b> ${data.temperature_f} °F</p>

<p><b>Humidity:</b> ${data.humidity}%</p>

<p><b>Weather:</b> ${data.description}</p>

<p><b>Wind Speed:</b> ${data.wind} m/s</p>

`;

}