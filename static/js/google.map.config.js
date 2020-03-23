// Google Maps
//-----------------------------------------------
var marker;

function initMap() {
  var myLatlng = {lat: 40.995875, lng: 29.137558};

  var map = new google.maps.Map(document.getElementById('map-canvas'), {
    zoom: 11,
    center: myLatlng
  });

  marker = new google.maps.Marker({
    map: map,
    animation: google.maps.Animation.DROP,
    position: {lat: 40.995875, lng: 29.137558}
  });

  marker.addListener('click', function() {
    map.setZoom(16);
    map.setCenter(marker.getPosition());
  });
} // End document ready