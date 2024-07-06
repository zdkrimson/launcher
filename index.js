window.addEventListener('pywebviewready', function() {
	console.log(window.pywebview.api.get_host())
	var iframe = document.getElementById('windowiframe');
	iframe.contentWindow.postMessage(window.pywebview.api.get_host(), '*');
});

function settings(status) {
	var settingsmenu = document.getElementById("settings");

	if (status == "show") {
		settingsmenu.classList.add("popup");
		settingsmenu.classList.remove("popout");
	}
	
	if (status == "hide") {
		settingsmenu.classList.remove("popup");
		settingsmenu.classList.add("popout");
	}
}

function help(status) {
	var helpmenu = document.getElementById("help");

	if (status == "show") {
		helpmenu.classList.add("popup");
		helpmenu.classList.remove("popout");
	}
	
	if (status == "hide") {
		helpmenu.classList.remove("popup");
		helpmenu.classList.add("popout");
	}
}

// Listen for messages from iframe
window.addEventListener('message', function(event) {
    // Verify origin of the iframe (optional, for security)
    // if (event.origin !== 'https://your-iframe-domain.com') return;

    // Check the message received from iframe
    if (event.data === 'hideSettings') {
        // Call settings function in the parent window
        settings('hide');
    }

    if (event.data === 'hideDocs') {
        // Call help function in the parent window
        help('hide');
    }
});
