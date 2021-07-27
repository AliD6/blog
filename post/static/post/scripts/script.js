
var request = new XMLHttpRequest;
request.open('GET', 'scripts/data.json');
request.onreadystatechange = function () {
    if ((request.readyState == 4) && (request.status == 200)) {
        var items = JSON.parse(request.responseText);
        console.log(items);
        var x = document.getElementById("demo");
        x.innerHTML="مکان: " +items[0].place[2] +"<br/>"  ;
        x.innerHTML+="تاریخ: " + items[0].date[2] + " " +items[0].time[2];
        console.log(items[0].place.length);
        

    }
}




request.send()