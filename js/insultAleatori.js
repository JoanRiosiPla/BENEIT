// Joan Rios i Pla - 2023 - _joanrios - contact.joanrios@gmail.com

// Get the domain
const domain = location.protocol + '//' + location.host + location.pathname;

// Get the search query
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
query = urlParams.get('search');

// Get elements
const searchBar = document.getElementById("searchBar");
const searchX = document.getElementById("search-x");

// Show X if there is a query
if (query) {
    searchX.classList.remove("hidden");
}

var data;
// Get insults.json
fetch('./insults.json?nocache=' + (new Date()).getTime())
.then(response => response.json())
.then(jsonData => {
    console.log('Fetched insults.json');
    data = jsonData; 
    // Insult ràndom
    const insult = data.insults[Math.floor(Math.random() * data.insults.length)];
    insultEl = document.getElementById("insultAleatori");
    if (insultEl) {
        insultEl.innerHTML = insult.paraula;
    }
    insultEl = document.getElementById("insultAleatoriDefinicio");
    if (insultEl) {
        insultEl.innerHTML = insult.definicio;
    }
    insultEl = document.getElementById("insultAleatoriFont");
    if (insultEl) {
        insultEl.innerHTML = insult.font.nom;
        insultEl.href = insult.font.url;
    }

});

function updateRandom() {
    // Insult ràndom
    if (data == undefined) {
        return;
    }
    const insult = data.insults[Math.floor(Math.random() * data.insults.length)];
    insultEl = document.getElementById("insultAleatori");
    if (insultEl) {
        insultEl.innerHTML = insult.paraula;
    }
    insultEl = document.getElementById("insultAleatoriDefinicio");
    if (insultEl) {
        insultEl.innerHTML = insult.definicio;
    }
    insultEl = document.getElementById("insultAleatoriFont");
    if (insultEl) {
        insultEl.innerHTML = insult.font.nom;
        insultEl.href = insult.font.url;
    }
}