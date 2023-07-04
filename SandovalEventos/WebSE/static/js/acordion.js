function openServ(evt, servName) {
  var i, tabMatricontent, tablinks;
  tabMatricontent = document.getElementsByClassName("tabMatricontent");
  for (i = 0; i < tabMatricontent.length; i++) {
    tabMatricontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(servName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();


// Bar
function openSubServBar(evt, SubServName) {
  var i, tabSubServContentBar, tablinksSubServBar;
  tabSubServContentBar = document.getElementsByClassName("tabSubServContentBar");
  for (i = 0; i < tabSubServContentBar.length; i++) {
    tabSubServContentBar[i].style.display = "none";
  }
  tablinksSubServBar = document.getElementsByClassName("tablinksSubServBar");
  for (i = 0; i < tablinksSubServBar.length; i++) {
    tablinksSubServBar[i].className = tablinksSubServBar[i].className.replace(" active", "");
  }
  document.getElementById(SubServName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenSubServBar").click();

// Aperitivos
function openSubServAperitivos(evt, SubServName) {
  var i, tabSubServContentAperitivos, tablinksSubServAperitivos;
  tabSubServContentAperitivos = document.getElementsByClassName("tabSubServContentAperitivos");
  for (i = 0; i < tabSubServContentAperitivos.length; i++) {
    tabSubServContentAperitivos[i].style.display = "none";
  }
  tablinksSubServAperitivos = document.getElementsByClassName("tablinksSubServAperitivos");
  for (i = 0; i < tablinksSubServAperitivos.length; i++) {
    tablinksSubServAperitivos[i].className = tablinksSubServAperitivos[i].className.replace(" active", "");
  }
  document.getElementById(SubServName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenSubServAperitivos").click();

// Entrada
function openSubServEntrada(evt, SubServName) {
  var i, tabSubServContentEntrada, tablinksSubServEntrada;
  tabSubServContentEntrada = document.getElementsByClassName("tabSubServContentEntrada");
  for (i = 0; i < tabSubServContentEntrada.length; i++) {
    tabSubServContentEntrada[i].style.display = "none";
  }
  tablinksSubServEntrada = document.getElementsByClassName("tablinksSubServEntrada");
  for (i = 0; i < tablinksSubServEntrada.length; i++) {
    tablinksSubServEntrada[i].className = tablinksSubServEntrada[i].className.replace(" active", "");
  }
  document.getElementById(SubServName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenSubServEntrada").click();

// Plato Principal
function openSubServPrincipal(evt, SubServName) {
  var i, tabSubServContentPrincipal, tablinksSubServPrincipal;
  tabSubServContentPrincipal = document.getElementsByClassName("tabSubServContentPrincipal");
  for (i = 0; i < tabSubServContentPrincipal.length; i++) {
    tabSubServContentPrincipal[i].style.display = "none";
  }
  tablinksSubServPrincipal = document.getElementsByClassName("tablinksSubServPrincipal");
  for (i = 0; i < tablinksSubServPrincipal.length; i++) {
    tablinksSubServPrincipal[i].className = tablinksSubServPrincipal[i].className.replace(" active", "");
  }
  document.getElementById(SubServName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenSubServPrincipal").click();

// Vajilla y Cristaleria
function openSubServVyC(evt, SubServName) {
  var i, tabSubServContentVyC, tablinksSubServVyC;
  tabSubServContentVyC = document.getElementsByClassName("tabSubServContentVyC");
  for (i = 0; i < tabSubServContentVyC.length; i++) {
    tabSubServContentVyC[i].style.display = "none";
  }
  tablinksSubServVyC = document.getElementsByClassName("tablinksSubServVyC");
  for (i = 0; i < tablinksSubServVyC.length; i++) {
    tablinksSubServVyC[i].className = tablinksSubServVyC[i].className.replace(" active", "");
  }
  document.getElementById(SubServName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenSubServVyC").click();

// Decoracion
function openSubServDeco(evt, SubServName) {
  var i, tabSubServContentDeco, tablinksSubServDeco;
  tabSubServContentDeco = document.getElementsByClassName("tabSubServContentDeco");
  for (i = 0; i < tabSubServContentDeco.length; i++) {
    tabSubServContentDeco[i].style.display = "none";
  }
  tablinksSubServDeco = document.getElementsByClassName("tablinksSubServDeco");
  for (i = 0; i < tablinksSubServDeco.length; i++) {
    tablinksSubServDeco[i].className = tablinksSubServDeco[i].className.replace(" active", "");
  }
  document.getElementById(SubServName).style.display = "block";
  evt.currentTarget.className += " active";
}
document.getElementById("defaultOpenSubServDeco").click();





// 