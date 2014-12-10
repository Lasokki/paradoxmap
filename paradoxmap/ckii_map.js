var map = L.map('map', {
    crs: L.CRS.Simple
}).setView([-175, 75], 2);

//height
var sw = map.unproject([0,3072], map.getMinZoom());
//width
var ne = map.unproject([2048,0], map.getMinZoom());

//map.setMaxBounds(new L.LatLngBounds(sw, ne));

L.tileLayer('outlines/{z}/{x}/{y}.png', {
    minZoom: 0,
    maxZoom: 6,
    attribution: 'Paradox Interactive / Erkki Mattila',
    tms: true,
    continuousWorld: true
}).addTo(map);

// Infothingie

// Control, that shows stuff when hovered on
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
};

info.update = function (props) {
    this._div.innerHTML = '<h4>Töki ja klikkaa monikulmiota, niin näet jotain</h4>' +  (props ? props.name: "");
};

info.addTo(map);

// GeoJSON-STUFF

function getColor(n) {
    return n == 'Saapasmaa' ? 'green' :
	   n == "L'Hexagone" ? 'blue' :
	   n == "Ultima Thule" ? 'orange' :
	   'red';
}

function style(feature) {
    return {
	fillColor: getColor(feature.properties.name),
        weight: 2,
        opacity: 1,
        color: 'red',
        dashArray: '3',
        fillOpacity: 0.5
    };
}

// GeoJSON listeners

function highlightFeature(e) {
    var layer = e.target;


    layer.setStyle({
        weight: 3,
        color: 'red',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties);
}

var geojson;

function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
	mouseover: highlightFeature,
	mouseout: resetHighlight,
	click: zoomToFeature
    });
}

geojson = L.geoJson(provdata, {
    style: style,
    onEachFeature: onEachFeature
}).addTo(map);

// RANDOM MARKERS
/*
var m1 = {
  x: 256, 
  y: 256
}
var mark1 = L.marker(map.unproject([m1.x, m1.y], map.getMinZoom())).addTo(map);

var m2 = {
  x: 0, 
  y: 256
}
var mark2 = L.marker(map.unproject([m2.x, m2.y], map.getMinZoom())).addTo(map);

var m3 = {
  x: 0, 
  y: 128
}

var mark3 = L.marker(map.unproject([m3.x, m3.y], map.getMinZoom())).addTo(map);

var popup = L.popup();

var dep = { x: 404, y: 120 }

var herp = L.popup()
    .setLatLng(map.unproject([256, 128], map.getMinZoom()))
    .setContent("LOL I'M DUMB")
    .openOn(map);

*/
// LAT-LONG POPUP
/*
function onMapClick(e) {
    popup
	.setLatLng(e.latlng)
	.setContent("You clicked the map at " + e.latlng.toString())
	.openOn(map);
}

map.on('click', onMapClick);
*/
