var ccolor = 0;
var btncompt = 0;

function click1(color) {
    var mon_element = document.getElementById('msg');
    ccolor = ccolor % 2;
    if (ccolor == 0) {
        mon_element.setAttribute("class", "ok0");
    } else {
        mon_element.setAttribute("class", "ok1");
    }
    ccolor++;

    addCanvas();
}

function addCanvas() {
    document.querySelector('');
    document.createElement(canvas)
}


var btn = mon_element = document.getElementById("ok2");
btn.addEventListener('click', click2);
var i = 0;
var span1 = document.getElementById("msg");

function click2() {
    i = document.getElementById("msg").innerHTML;
    btncompt++;
    span1.innerHTML += "<br>Ajout du message numéro" + btncompt;
    console.log(i);
}

document.getElementById("ok3").addEventListener('click', click3);

function click3() {
    span1.innerHTML = "";
    X = 1;
    btncompt = 0;
}