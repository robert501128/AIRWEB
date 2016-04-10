// initialize the map
var map = L.map('map').setView([23.7859146, 120.9945463], 8);

// load a tile layer
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}',
{
  accessToken: 'pk.eyJ1Ijoicm9iZXJ0NTAxMTI4IiwiYSI6ImNpbWdkc2V5dDAxejh2Y202cHNrcDQwcTIifQ.U3Me8efJmnVkr8rMvPf0ww',
  id: 'robert501128.pi9kohoa',
  maxZoom: 17,
  minZoom: 5
}).addTo(map);


// varaiables
lassMarkers = [] // all the marker added to map

// add devices locations
for(var i = 0; i < lassLocs.length; i++) {
    var newMarker = L.marker(lassLocs[i]).addTo(map);
    lassMarkers.push(newMarker);
}

