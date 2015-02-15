var map = L.map('map', {
    crs: L.CRS.Simple
}).setView([-800, 800], 0);

//map.setMaxBounds(new L.LatLngBounds(sw, ne));

L.tileLayer('', {
    minZoom: 0,
    maxZoom: 2,
    attribution: 'Paradox Interactive / Erkki Mattila',
    tms: true,
    continuousWorld: true
}).addTo(map);


// Controls

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
};

info.update = function (props, id, culture, religion) {
    this._div.innerHTML = '<a href="../paradoxmap_info/">What is this thing?</a><br><br><a href="https://github.com/Lasokki/paradoxmap">GitHub</a><br><h4>Click on a province to zoom in</h4>' + (props ? props.name: "") + '<br>' + (id ? id: "") + '<br>' + (culture ? culture: "") + '<br>' + (religion ? religion:"");
};

var mapmodes = L.control();

var current_mapmode = "religions";

mapmodes.onAdd = function(map) {
    this._div = L.DomUtil.create('div', 'mapmode');
    this.update();
    return this._div;
};

mapmodes.update = function() {
    this._div.innerHTML = '<p>Religions</p><button onClick="showReligions()">Religions</button><button onClick="showCultures()">Cultures</button>';
};

//mapmodes.setPosition('');
mapmodes.addTo(map);
info.addTo(map);

function showCultures() {
    geojson.setStyle(style_cultures);
    mapmodes._div.childNodes[0].innerHTML = "Cultures"
    current_mapmode = "cultures"
}

function showReligions() {
    geojson.setStyle(style_religions);
    mapmodes._div.childNodes[0].innerHTML = "Religions"
    current_mapmode = "religions"
}

// GeoJSON-STUFF

function getCultureColours(n, culture) {
    return n == "" ? "black" :
	culture_colours[culture];
}

function getReligionColours(n, religion) {
    return n == "" ? "black" :
	religion_colours[religion];
}

function style_religions(feature) {
    return {
	fillColor: getReligionColours(feature.properties.name, religions[feature.id]),
        weight: 2,
        opacity: 1,
        color: 'maroon',
        dashArray: '3',
        fillOpacity: 0.9
    };
}

function style_cultures(feature) {
    return {
	fillColor: getCultureColours(feature.properties.name, cultures[feature.id]),
        weight: 2,
        opacity: 1,
        color: 'maroon',
        dashArray: '3',
        fillOpacity: 0.9
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
    info.update(layer.feature.properties, layer.feature.id, cultures[layer.feature.id], religions[layer.feature.id]);
}

var geojson;

function resetHighlight(e) {

    var layer = e.target;
    
    if (current_mapmode == "cultures")
	layer.setStyle(style_cultures(layer.feature));
    else
	layer.setStyle(style_religions(layer.feature));

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
    style: style_religions,
    onEachFeature: onEachFeature
}).addTo(map);
