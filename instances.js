console.log("'instances.js' loaded successfully")

function loadInstance(name, version, icon) {
	const a = document.createElement('a');
	const div = document.createElement('div');
	div.className = 'instance';

	// Attach version as a data attribute
    a.setAttribute('instance-version', version);

    a.onclick = function() {
    	selectInstance(name, version);
    }

	const img = document.createElement('img');
	img.width = 50;
	if (icon === 'default') {
		img.src = 'assets/icons/grass.svg';
	}

	const p = document.createElement('p');
	p.textContent = name;

	div.appendChild(img);
	div.appendChild(p);
	a.appendChild(div);

	const instances = document.querySelector('.instances');
	instances.appendChild(a);
}

// Adds information on load
document.addEventListener('DOMContentLoaded', function() {
	// lOADING VALUES
	setTimeout(function(){
		var rawinstancedata = localStorage.getItem('instancesdata')
		var instancesdata = JSON.parse(rawinstancedata);

		instancesdata.forEach(entry => {
			loadInstance(entry.name, entry.version, entry.icon)
		});
	}, 5000);
});

// function addInstance(name) {
// 	const a = document.createElement('a');
// 	const div = document.createElement('div');
// 	div.className = 'instance';

// 	const img = document.createElement('img');
// 	img.width = 50;
// 	img.src = 'assets/icons/grass.svg';

// 	const p = document.createElement('p');
// 	p.textContent = name;

// 	div.appendChild(img);
// 	div.appendChild(p);
// 	a.appendChild(div);

// 	const instances = document.querySelector('.instances');
// 	instances.appendChild(a);
// };

function closeCreation() {
	var bg = document.getElementById("dialogbg");
	var dialog = document.getElementById("newinst");

	dialog.classList.remove('popup');
	dialog.classList.add('popout');
	bg.classList.add('fadeout');
	bg.classList.remove('fadein');
}

function startInstance() {
	localStorage.setItem('launchname', window.__selectedName);
	localStorage.setItem('launchversion', window.__selectedVersion);
	window.parent.postMessage('launchminecraft', '*');
}

function selectInstance(name, version) {
	var start = document.getElementById("startinst");
	window.__selectedName = name
	window.__selectedVersion = version;
	// var edit = document.getElementById("editinst");

	start.disabled = false;
	// start.disabled = false;
}

function addInstance() {
	const a = document.createElement('a');
	const div = document.createElement('div');
	div.className = 'instance';

	// Attach version as a data attribute
    a.setAttribute('instance-version', document.getElementById('mcversions').value);

    a.onclick = function() {
    	selectInstance(document.getElementById('offlinename').value, document.getElementById('mcversions').value);
    }

	const img = document.createElement('img');
	img.width = 50;
	img.src = 'assets/icons/grass.svg';

	const p = document.createElement('p');
	p.textContent = document.getElementById('offlinename').value;

	div.appendChild(img);
	div.appendChild(p);
	a.appendChild(div);

	const instances = document.querySelector('.instances');
	instances.appendChild(a);

	localStorage.setItem('instance-name', document.getElementById('offlinename').value);
	localStorage.setItem('instance-version', document.getElementById('mcversions').value);
	localStorage.setItem('instance-icon', 'default');

	window.parent.postMessage('newinstance', '*');

	closeCreation();
};

// Adds information on load
document.addEventListener('DOMContentLoaded', function() {
	window.parent.postMessage('awaitInstance', '*');
	fetch('https://launchermeta.mojang.com/mc/game/version_manifest_v2.json')
	  .then(response => {
	    if (!response.ok) {
	      throw new Error('Network response was not ok');
	    }
	    return response.json();
	  })
	  .then(data => {
            const dropdown = document.getElementById('mcversions');
            const versions = data.versions;  // Access the versions array
            
            versions.forEach(version => {
                if (version.type === 'release') {  // Check if type is 'release'
                    const option = document.createElement('option');
                    option.value = version.id;
                    option.textContent = version.id;
                    dropdown.appendChild(option);
                }
            });
	  })
	  .catch(error => {
	    console.error('There was a problem with the fetch operation:', error);
	  });


});





function closeWindow() {
	window.parent.postMessage('hideInstances', '*');
}

function newInstance() {
	var bg = document.getElementById("dialogbg");
	var dialog = document.getElementById("newinst");

	bg.classList.add('fadein');
	bg.classList.remove('fadeout');
	dialog.classList.add('popup');
	dialog.classList.remove('popout');
}