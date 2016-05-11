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

// custom icons
var safeIcon = L.icon({
    iconUrl: '/static/dot/cd1.png',
    iconSize:     [20, 20], // size of the icon
    iconAnchor:   [10, 10], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

var warnIcon = L.icon({
    iconUrl: '/static/dot/cd3.png',
    iconSize:     [20, 20], // size of the icon
    iconAnchor:   [10, 10], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

var dangerIcon = L.icon({
    iconUrl: '/static/dot/cd7.png',
    iconSize:     [20, 20], // size of the icon
    iconAnchor:   [10, 10], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

// add devices locations
for(var i = 0; i < lassLocs.length; i++) {
    conf = {icon: safeIcon};
    if (sD0[i] > 35 ) { conf['icon'] = warnIcon; }
    if (sD0[i] > 50 ) { conf['icon'] = dangerIcon; }

    var newMarker = L.marker(lassLocs[i], conf).addTo(map);
    newMarker.bindPopup("<b>"+deviceId[i]+"</b><br>pm2.5: "+sD0[i]);
    lassMarkers.push(newMarker);
}
