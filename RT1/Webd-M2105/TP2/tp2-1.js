var jours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var tmin = [7.0, 7.0, 4.4, 2.7, 8.2, 2.3, 4.1, 5.5, 11.6, 8.2];
var wind = [68.5, 79.6, 42.6, 64.8, 50.0, 18.5, 18.5, 38.9, 38.9, 35.2];

var courbe1 = {
    label: "Température minimum en °C",
    backgroundColor: "darkcyan",
    borderColor: "darkcyan",
    data: tmin,
    pointRadius: 5,
    pointHoverRadius: 10,
    fill: false
};
var courbe2 = {
    label: "Vitesse du vent",
    backgroundColor: "darkorchid",
    borderColor: "darkorchid",
    data: wind,
    pointRadius: 5,
    pointHoverRadius: 10,
    fill: false
};
var config = {
    type: "line",
    data: { labels: jours, datasets: [courbe1] },
    options: {
        title: { display: true, text: "Béziers en 2007" },
        tooltips: { mode: "index", intersect: false }
    }
};

config.data.datasets.push(courbe2);

window.onload = function() {
    var ctx = document.getElementById("canvas").getContext("2d");
    window.graph1 = new Chart(ctx, config);
};


var colors = ["black", "yellow", "blue", "magenta", "aqua", "coral", "red", "chartreuse"];
for (var i = 0; i < colors.length; i++) {
    console.log(colors[i]);

    var myoption = document.createElement("option");
    myoption.setAttribute("value", "i");
    myoption.innerHTML = colors[i];

    var myselect = document.getElementById("couleur");
    myselect.appendChild(myoption);
}


var selectCouleur = document.getElementById("couleur");
selectCouleur.addEventListener("change", function() {
    var val = this.options[this.selectedIndex].value;
    var txt = this.options[this.selectedIndex].text;
    console.log("Couleur " + this.selectedIndex + ": " + val + " -> " + txt);
    courbe1.backgroundColor = txt;
    courbe1.borderColor = txt;
    window.graph1.update();
});


var axeX = {
    display: true,
    scaleLabel: { display: true, labelString: "Numéro du jour" }
};
var axeY = {
    display: true,
    scaleLabel: { display: true, labelString: "Température en °C" }
};
config.options.scales = { xAxes: [axeX], yAxes: [axeY] };


document.getElementById("axes").addEventListener("change", function() {
    config.options.scales.xAxes[0].scaleLabel.display = this.checked;
    config.options.scales.yAxes[0].scaleLabel.display = this.checked;
    window.graph1.update();
})

var axeY1 = {
    id: "yTmin",
    position: "left",
    ticks: { suggestedMin: 2, suggestedMax: 12 },
    display: true,
    scaleLabel: { display: true, labelString: "Température en °C" }
};

var axeY2 = {
    id: "yWind",
    position: "right",
    ticks: { suggestedMin: 2, suggestedMax: 12 },
    display: true,
    scaleLabel: { display: true, labelString: "Vitesse en km/h" },
    gridLines: { drawOnChartArea: false }
};

courbe1.yAxisID = "yTmin";
courbe2.yAxisID = "yWind";
config.options.scales.yAxes = [axeY1, axeY2];