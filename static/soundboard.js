

const rain = new Audio("/static/sounds/rain.mp3");
rain.loop = true;
const waves = new Audio("/static/sounds/waves.mp3");
waves.loop = true;
const fire = new Audio("/static/sounds/fire.mp3");
fire.loop = true;
const forest = new Audio("/static/sounds/forest.mp3");
forest.loop = true;
const lofi = new Audio("/static/sounds/lo-fi.mp3");
lofi.loop = true;
const brown = new Audio("/static/sounds/brownnoise.mp3");
brown.loop = true;

// Rain controls
document.getElementById("rain-slider").oninput = function() {
    rain.volume = this.value / 100;
};
document.getElementById("rain-play").onclick = () => rain.play();
document.getElementById("rain-pause").onclick = () => rain.pause();

// Waves controls
document.getElementById("waves-slider").oninput = function() {
    waves.volume = this.value / 100;
};
document.getElementById("waves-play").onclick = () => waves.play();
document.getElementById("waves-pause").onclick = () => waves.pause();

// Fire controls
document.getElementById("fire-slider").oninput = function() {
    fire.volume = this.value / 100;
};
document.getElementById("fire-play").onclick = () => fire.play();
document.getElementById("fire-pause").onclick = () => fire.pause();

// Lofi controls
document.getElementById("lofi-slider").oninput = function() {
    lofi.volume = this.value / 100;
};
document.getElementById("lofi-play").onclick = () => lofi.play();
document.getElementById("lofi-pause").onclick = () => lofi.pause();

// Forest controls
document.getElementById("forest-slider").oninput = function() {
    forest.volume = this.value / 100;
};
document.getElementById("forest-play").onclick = () => forest.play();
document.getElementById("forest-pause").onclick = () => forest.pause();

// Brown controls
document.getElementById("brown-slider").oninput = function() {
    brown.volume = this.value / 100;
};
document.getElementById("brown-play").onclick = () => brown.play();
document.getElementById("brown-pause").onclick = () => brown.pause();

