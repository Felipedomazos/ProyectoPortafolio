function openPage(pageName, elmnt) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByName("tab");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
        if (tablinks[i].value == pageName) {
            tablinks[i].checked = true;
        }
    }
    document.getElementById(pageName).style.display = "block";
}


function toggleAdditionalButtonsT() {
    const additionalButtonsT = document.querySelector('.additional-buttons-t');
    additionalButtonsT.style.display = additionalButtonsT.style.display === 'block' ? 'none' : 'block';
}
function toggleAdditionalButtonsD(){
    const additionalButtonsD = document.querySelector('.additional-buttons-d');
    additionalButtonsD.style.display = additionalButtonsD.style.display === 'block' ? 'none' : 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('.topnav a');

    links.forEach(function(link) {
        link.addEventListener('click', function() {
            // Removemos la clase 'active' de todos los enlaces
            links.forEach(function(link) {
                link.classList.remove('active');
            });

            // Agregamos la clase 'active' al enlace clicado
            this.classList.add('active');
        });
    });
});
