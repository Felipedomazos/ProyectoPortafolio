// Tipo Celebracion
function openTipoCeleb(evt, celebName) {
    var i, tabCelebContent, tablinks;
    tabCelebContent = document.getElementsByClassName("tabCelebContent");
    for (i = 0; i < tabCelebContent.length; i++) {
        tabCelebContent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(celebName).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenCeleb").click();

// Opciones Cumpleaños
function openCumple(evt, cumpleName) {
    var i, tabContentCumple, tablinksCumple;
    tabContentCumple = document.getElementsByClassName("tabContentCumple");
    for (i = 0; i < tabContentCumple.length; i++) {
        tabContentCumple[i].style.display = "none";
    }
    tablinksCumple = document.getElementsByClassName("tablinksCumple");
    for (i = 0; i < tablinksCumple.length; i++) {
        tablinksCumple[i].className = tablinksCumple[i].className.replace(" active", "");
    }
    document.getElementById(cumpleName).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenCumple").click();

// Opciones Aniversario
function openAniv(evt, anivName) {
    var i, tabContentAniv, tablinksAniv;
    tabContentAniv = document.getElementsByClassName("tabContentAniv");
    for (i = 0; i < tabContentAniv.length; i++) {
        tabContentAniv[i].style.display = "none";
    }
    tablinksAniv = document.getElementsByClassName("tablinksAniv");
    for (i = 0; i < tablinksAniv.length; i++) {
        tablinksAniv[i].className = tablinksAniv[i].className.replace(" active", "");
    }
    document.getElementById(anivName).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenAniv").click();

// Opciones Fiesta
function openFiesta(evt, fiestaName) {
    var i, tabContentFiesta, tablinksFiesta;
    tabContentFiesta = document.getElementsByClassName("tabContentFiesta");
    for (i = 0; i < tabContentFiesta.length; i++) {
        tabContentFiesta[i].style.display = "none";
    }
    tablinksFiesta = document.getElementsByClassName("tablinksFiesta");
    for (i = 0; i < tablinksFiesta.length; i++) {
        tablinksFiesta[i].className = tablinksFiesta[i].className.replace(" active", "");
    }
    document.getElementById(fiestaName).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenFiesta").click();