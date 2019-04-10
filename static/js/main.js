var res = str?str.split(","):"";
var v0 = parseFloat(res[0]);
var v1 = parseFloat(res[1]);
document.getElementById("demo").innerHTML = v0 + "<br>" + v1; 

function initMap() {
    var map = set_my_position();
    points.forEach(p => {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(p.x_coord, p.y_coord),
            map: map,
        })
    });
}

function set_my_position(){
    var myLatlng;
    if( v0 !== null || v1 !== null ) {
      myLatlng = {lat: v0, lng: v1};
    } else {
      myLatlng = {lat: 1.352660, lng: 103.861821};
    }  
    var map = new google.maps.Map(document.getElementById('googleMap'), {
        zoom: zoom,
        center: myLatlng
    });
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(myLatlng.lat, myLatlng.lng),
        map: map,
        title: 'Click to zoom',
        icon: "/static/icons/image.png"
    });
    
    map.addListener('center_changed', function() {
    window.setTimeout(function() {
        map.panTo(marker.getPosition());
    }, 3000);
    });
    
    var cityCircle = new google.maps.Circle({
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 1,
        fillColor: '#FF0000',
        fillOpacity: 0.35,
        map: map,
        center: {lat: v0, lng: v1},
        radius: circleSize*1
    });

    marker.addListener('click', function() {
        map.setZoom(15);
        map.setCenter(marker.getPosition());
    });
    return map
}