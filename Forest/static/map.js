// Initialize the map
var map = L.map('map').setView([0, 0], 5); // Set initial center and zoom level

// Add a tile layer (e.g., OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Sample forest data (replace this with your actual data)
var forests = [
    { name: 'Forest 1', lat: -1.292066, lon: 36.821945},
    { name: 'Forest 2', lat: 0.45, lon: 36.32 },
    // Add more forest data as needed
];

// Add markers for each forest
forests.forEach(function (forest) {
    L.marker([forest.lat, forest.lon]).addTo(map)
        .bindPopup('<b>' + forest.name + '</b><br>Coordinates: ' + forest.lat + ', ' + forest.lon)
        .openPopup();
});
