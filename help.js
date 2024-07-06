function closeHelp() {
	// Send message from iframe to parent window
	window.parent.postMessage('hideDocs', '*');
}

document.addEventListener('DOMContentLoaded', function() {
	if (window.self === window.top) {
	    // Not inside an iframe
	    document.body.style.backgroundColor = 'darkred';
	}
});