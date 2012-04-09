var lat=50;
var lon=-110;

/*
 * This is a simple google maps window if you want to add more features look for
 * google maps api documentation.
 */
function load() {
    if (GBrowserIsCompatible()) {
        var map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(lat, lon), 13);
    }
}

//this is my show map function with specific coordinates
function map(position) {
    // first we update our long and lat
    lat = position.coords.latitude;
    //and show the new map
    lon = position.coords.longitude;
    load();
}
//
//this function retrieves the position data from browser
function get_location() {
    navigator.geolocation.getCurrentPosition(map);
}

