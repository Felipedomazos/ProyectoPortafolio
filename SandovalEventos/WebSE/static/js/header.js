function openSidebar() {
	document.querySelector('.sidebar').classList.add('sidebar-open');
}

function closeSidebar() {
	document.querySelector('.sidebar').classList.remove('sidebar-open');
}

document.addEventListener('click', function (event) {
	var sidebar = document.querySelector('.sidebar');
	if (event.target.closest('.sidebar-container') === null && sidebar.classList.contains('sidebar-open')) {
		sidebar.classList.remove('sidebar-open');
	}
});


var modal = document.getElementById('id01');

