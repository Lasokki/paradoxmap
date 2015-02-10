var map = L.map('map', {
    crs: L.CRS.Simple
}).setView([-800, 800], 0);

//height
var sw = map.unproject([0,3072], map.getMinZoom());
//width
var ne = map.unproject([2048,0], map.getMinZoom());

//map.setMaxBounds(new L.LatLngBounds(sw, ne));

L.tileLayer('', {
    minZoom: 0,
    maxZoom: 2,
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

info.update = function (props, id) {
    this._div.innerHTML = '<a href="../paradoxmap_info/">What is this thing?</a><br><br><a href="https://github.com/Lasokki/paradoxmap">GitHub</a><br><h4>Click on a province to zoom in</h4>' + (props ? props.name: "") + '<br>' + (id ? id: "");
};

info.addTo(map);

// GeoJSON-STUFF

function getColor(n) {
    return n == "" ? "black" :
	'maroon';
}

function style(feature) {
    return {
	fillColor: getColor(feature.properties.name),
        weight: 2,
        opacity: 1,
        color: 'maroon',
        dashArray: '3',
        fillOpacity: 0.4
    };
}

// GeoJSON listeners

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 1,
        color: 'red',
        dashArray: '',
        fillOpacity: 1
    });

    if (!L.Browser.ie && !L.Browser.opera) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties, layer.feature.id);
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

geojson = L.geoJson(ckii_provdata, {
    style: style,
    onEachFeature: onEachFeature
}).addTo(map);
