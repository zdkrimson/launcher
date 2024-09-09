console.log("'settings.js' loaded successfully")

// Adds information on load
document.addEventListener('DOMContentLoaded', function() {
	window.parent.postMessage('awaitConfig', '*');
	var restext = document.getElementById('sysres');
	var platformtext = document.getElementById('sysplat');
	var syshost = document.getElementById('syshost');
	var sysmem = document.getElementById("sysmem");
	var sysgpu = document.getElementById("sysgpu");
	var syscpu = document.getElementById("syscpu");
	var defjava = document.getElementById("defaultjava");
	var launcher = document.getElementById("launcher");
	
	// lOADING VALUES
	restext.textContent = "Resolution: " + window.screen.width + "x" + window.screen.height;
	platformtext.textContent = "Platform: " + navigator.platform;
	launcher.classList.add("fadein");
	setTimeout(function(){
		syshost.textContent = "Host: " + localStorage.getItem('hostmachine');
		sysmem.textContent = "Memory: " + localStorage.getItem('sysmem');
		sysgpu.textContent = "GPU: " + localStorage.getItem('sysgpu');
		syscpu.textContent = "CPU: " + localStorage.getItem('syscpu');
		document.getElementById('mcmaximized').checked = JSON.parse(localStorage.getItem('maximizedefault'));
		document.getElementById('mcdemomode').checked = JSON.parse(localStorage.getItem('demomode'));
		document.getElementById('mcmulti').checked = JSON.parse(localStorage.getItem('multiplayer'));
		document.getElementById('mcchat').checked = JSON.parse(localStorage.getItem('gamechat'));
		// document.getElementById('').checked = localStorage.getItem('customtheme'); unimplemented
		document.getElementById('javapath').value = localStorage.getItem('javapath'); 
		document.getElementById('jvmargs').value = localStorage.getItem('jvmargs'); 
		document.getElementById('minram').value = localStorage.getItem('minmem'); 
		document.getElementById('maxram').value = localStorage.getItem('maxmem'); 
		document.getElementById('windowwidth').value = localStorage.getItem('winwidth'); 
		document.getElementById('windowheight').value = localStorage.getItem('winheight'); 
		defjava.textContent = "Default Java: " + localStorage.getItem('javapath');
		document.getElementById('accountload').remove();
	}, 3000);
});

// window.addEventListener('message', function(event) {
// 	console.log(event)
// 	console.log(event.data)
// });

function closeSettings() {
	// Saving Settings
	localStorage.setItem('maximizedefault', document.getElementById('mcmaximized').checked);
	localStorage.setItem('demomode', document.getElementById('mcdemomode').checked);
	localStorage.setItem('multiplayer', document.getElementById('mcmulti').checked);
	localStorage.setItem('gamechat', document.getElementById('mcchat').checked);
	// localStorage.setItem('customtheme', document.getElementById('mcmaximized').checked); (not implemented)
	localStorage.setItem('javapath', document.getElementById('javapath').value);
	localStorage.setItem('jvmargs', document.getElementById('jvmargs').value);
	localStorage.setItem('minmem', document.getElementById('minram').value);
	localStorage.setItem('maxmem', document.getElementById('maxram').value);
	localStorage.setItem('winwidth', document.getElementById('windowwidth').value);
	localStorage.setItem('winheight', document.getElementById('windowheight').value);

	// Send message from iframe to parent window
	window.parent.postMessage('hideSettings', '*');
}

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

function addaccount() {
	var bg = document.getElementById("dialogbg");
	var dialog = document.getElementById("addacc");

	bg.classList.remove('fadeout');
	dialog.classList.remove('popout');
	bg.classList.add('fadein');
	dialog.classList.add('popup');
}

function closeAddAccount() {
	var bg = document.getElementById("dialogbg");
	var dialog = document.getElementById("addacc");

	bg.classList.add('fadeout');
	dialog.classList.add('popout');
	bg.classList.remove('fadein');
	dialog.classList.remove('popup');
}

function mslogin() {
	var bg = document.getElementById("dialogbg");
	var dialog = document.getElementById("addacc");
	var msdialog = document.getElementById("addmicrosoft");

	msdialog.classList.add('popup');
	msdialog.classList.remove('popout');
	dialog.classList.remove('popup');
	dialog.classList.add('popout');
}

function closeMSAccount() {
	var bg = document.getElementById("dialogbg");
	var msdialog = document.getElementById("addmicrosoft");

	msdialog.classList.remove('popup');
	msdialog.classList.add('popout');
	bg.classList.add('fadeout');
	bg.classList.remove('fadein');
}

function offlinelogin() {
	var bg = document.getElementById("dialogbg");
	var dialog = document.getElementById("addacc");
	var offlinedialog = document.getElementById("addoffline");

	offlinedialog.classList.add('popup');
	offlinedialog.classList.remove('popout');
	dialog.classList.remove('popup');
	dialog.classList.add('popout');
}

function closeOfflineAccount() {
	var bg = document.getElementById("dialogbg");
	var offlinedialog = document.getElementById("addoffline");

	offlinedialog.classList.remove('popup');
	offlinedialog.classList.add('popout');
	bg.classList.add('fadeout');
	bg.classList.remove('fadein');
}

function login(method) {
	if (method == 'offline') {
		console.log('Logging In... (Offline Mode)')
		console.log('Offline Name: ' + document.getElementById('offlinename').value)
		console.log('Offline UUID: ' + document.getElementById('offlineuuid').value)
		localStorage.setItem('offlineusername', document.getElementById('offlinename').value);
		localStorage.setItem('offlineuuid', document.getElementById('offlineuuid').value);
		// document.createElement('div'); (i'll get this workin soon)
		window.parent.postMessage('offlinelogin', '*');
		displayAccount(document.getElementById('offlinename').value, document.getElementById('offlineuuid').value);
		closeOfflineAccount();
	}

	if (method == 'microsoft') {
		console.log('Not Implemented (Microsoft Login)');
	}
}

function selectAccount(name, uuid) {
	localStorage.setItem('current-username', name);
	localStorage.setItem('current-uuid', uuid);
	window.parent.postMessage('accountchange', '*');
}

function displayAccount(name, uuid, linkUrl) {
    const accountDiv = document.createElement('div');
    accountDiv.className = 'account';

    const linkElement = document.createElement('a');
    linkElement.className = 'account-link';

    const usernameP = document.createElement('p');
    usernameP.textContent = `Username: ${name}`;

    const uuidP = document.createElement('p');
    uuidP.className = 'small-text';

    if (!uuid || !uuid.trim()) {
        uuidP.textContent = 'UUID: Unset';
    } else {
        uuidP.textContent = `UUID: ${uuid}`;
    }

    linkElement.appendChild(usernameP);
    linkElement.appendChild(uuidP);

    accountDiv.appendChild(linkElement);

    const accountsSection = document.getElementById('account-section');

    accountsSection.appendChild(accountDiv);

	linkElement.addEventListener('click', (event) => { selectAccount(name, uuid); });
}
