function closeSettings() {
	// Send message from iframe to parent window
	window.parent.postMessage('hideSettings', '*');
}

// Check if the webpage is not loaded inside an iframe



//This code snippet sets the background to dark red if ran outside an iframe, this makes writing the settings page easier without it being embedded?
// Im writing the settings page in it's own tab, not in the iframe cuz i need to refresh the page then open up the settings menu every new change
// Wait for DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
	var launcher = document.getElementById("launcher");
	launcher.classList.add('fadein');
	if (window.self === window.top) {
	    // Not inside an iframe
	    document.body.style.backgroundColor = 'darkred';
	}
});


function launcher() {
	var launcher = document.getElementById("launcher");
	var mc = document.getElementById("minecraft");
	var java = document.getElementById("java");
	var accounts = document.getElementById("accounts");
	var themes = document.getElementById("themes");
	var about = document.getElementById("about");

	launcher.classList.add("fadein");
	mc.classList.remove("fadein");
	java.classList.remove("fadein");
	accounts.classList.remove("fadein");
	themes.classList.remove("fadein");
	about.classList.remove("fadein");
}

function minecraft() {
	var launcher = document.getElementById("launcher");
	var mc = document.getElementById("minecraft");
	var java = document.getElementById("java");
	var accounts = document.getElementById("accounts");
	var themes = document.getElementById("themes");
	var about = document.getElementById("about");

	launcher.classList.remove("fadein");
	mc.classList.add("fadein");
	java.classList.remove("fadein");
	accounts.classList.remove("fadein");
	themes.classList.remove("fadein");
	about.classList.remove("fadein");
}

function java() {
	var launcher = document.getElementById("launcher");
	var mc = document.getElementById("minecraft");
	var java = document.getElementById("java");
	var accounts = document.getElementById("accounts");
	var themes = document.getElementById("themes");
	var about = document.getElementById("about");

	launcher.classList.remove("fadein");
	mc.classList.remove("fadein");
	java.classList.add("fadein");
	accounts.classList.remove("fadein");
	themes.classList.remove("fadein");
	about.classList.remove("fadein");
}

function accounts() {
	var launcher = document.getElementById("launcher");
	var mc = document.getElementById("minecraft");
	var java = document.getElementById("java");
	var accounts = document.getElementById("accounts");
	var themes = document.getElementById("themes");
	var about = document.getElementById("about");

	launcher.classList.remove("fadein");
	mc.classList.remove("fadein");
	java.classList.remove("fadein");
	accounts.classList.add("fadein");
	themes.classList.remove("fadein");
	about.classList.remove("fadein");
}

function themes() {
	var launcher = document.getElementById("launcher");
	var mc = document.getElementById("minecraft");
	var java = document.getElementById("java");
	var accounts = document.getElementById("accounts");
	var themes = document.getElementById("themes");
	var about = document.getElementById("about");

	launcher.classList.remove("fadein");
	mc.classList.remove("fadein");
	java.classList.remove("fadein");
	accounts.classList.remove("fadein");
	themes.classList.add("fadein");
	about.classList.remove("fadein");
}

function about() {
	var launcher = document.getElementById("launcher");
	var mc = document.getElementById("minecraft");
	var java = document.getElementById("java");
	var accounts = document.getElementById("accounts");
	var themes = document.getElementById("themes");
	var about = document.getElementById("about");

	launcher.classList.remove("fadein");
	mc.classList.remove("fadein");
	java.classList.remove("fadein");
	accounts.classList.remove("fadein");
	themes.classList.remove("fadein");
	about.classList.add("fadein");
}
