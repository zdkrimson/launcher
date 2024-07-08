document.addEventListener('DOMContentLoaded', function() {
	window.addEventListener('pywebviewready', function() {
		var lastuser = document.getElementById('lastuser');
		var lastinst = document.getElementById('instancename');
		pywebview.api.get_username('recent').then(function(result) {
			// it took me an ungodly amount of time to figure this out, im so pissed rn
			if (result == "") {
				lastuser.textContent = "Logged in as: Not Logged In!";
			} else {
				lastuser.textContent = "Logged in as: " + result;
			}
		});
		pywebview.api.get_recentinstance().then(function(result) {
			if (result == "") {
				lastinst.textContent = "Current Instance: Not Selected";
			} else {
				lastinst.textContent = "Current Instance: " + result;
			}
		});
		pywebview.api.get_host().then(function(result) {
			// it took me an ungodly amount of time to figure this out, im so pissed rn
			console.log('Host Machine: ' + result);
			localStorage.setItem('hostmachine', result);
		});
		pywebview.api.get_mem().then(function(result) {
			// i love copy n paste :)
			console.log('Memory: ' + result);
			localStorage.setItem('sysmem', result);
		});
		pywebview.api.get_gpu().then(function(result) {
			console.log('GPU: ' + result);
			localStorage.setItem('sysgpu', result);
		});
		pywebview.api.get_cpu().then(function(result) {
			console.log('CPU: ' + result);
			localStorage.setItem('syscpu', result);
		});
    });
});

// window.addEventListener('message', function(event) {
// 	if (event.data === 'awaitConfig') {
// 		console.log("'awaitConfig' Message from settings.js received by index.js")
// 		// Sending settings to iframe (settings.html)
// 		window.addEventListener('pywebviewready', function() {
// 			var settingsiframe = document.getElementById('settings');
// 			pywebview.api.get_settings().then(function(result) {
// 			    console.log(result);
// 			    var customtheme = result.customtheme;
// 			    var demomode = result.demomode;
// 			    var firsttime = result.firsttime;
// 			    var gamechat = result.gamechat;
// 			    var javapath =  result.javapath;
// 			    var jvmargs = result.jvmargs;
// 			    var lastaccount = result.lastaccount;
// 			    var lastinstance = result.lastinstance;
// 			    var maximizedefault = result.maximizedefault;
// 			    var minmem = result.minmem;
// 			    var maxmem = result.maxmem;
// 			    var multiplayer = result.multiplayer;
// 			    var winheight = result.winheight;
// 			    var winwidth = result.winwidth;
// 			    document.addEventListener('DOMContentLoaded', function() {
// 			    	console.log('Sending...')
// 			    	document.getElementById("settings").contentWindow.postMessage(result, '*'); // '*' allows sending to any origin
// 			    	console.log('Sent')
// 			    });
// 			});
// 		});
// 	}
// });

// window.addEventListener('message', function(event) {
//     if (event.data === 'awaitConfig') {
//         console.log("'awaitConfig' Message from settings.js received by index.js");

//         window.addEventListener('pywebviewready', function() {
//             var settingsiframe = document.getElementById('settings');
//             pywebview.api.get_settings().then(function(result) {
//                 console.log(result);
//                 settingsiframe.contentWindow.postMessage(result, '*');
//             }).catch(function(error) {
//                 console.error('Error fetching settings:', error);
//             });
//         });
//     }
// });

document.addEventListener('DOMContentLoaded', function() {
	window.addEventListener('message', function(event) {
		if (event.data === 'awaitConfig') {
			console.log("'awaitConfig' Message from settings.js received by index.js")
			// Sending settings to iframe (settings.html)
			window.addEventListener('pywebviewready', function() {
				var settingsiframe = document.getElementById('settings');
				pywebview.api.get_settings().then(function(result) {
				    console.log(result);
				    // var customtheme = result.customtheme;
				    // var demomode = result.demomode;
				    // var firsttime = result.firsttime;
				    // var gamechat = result.gamechat;
				    // var javapath =  result.javapath;
				    // var jvmargs = result.jvmargs;
				    // var lastaccount = result.lastaccount;
				    // var lastinstance = result.lastinstance;
				    // var maximizedefault = result.maximizedefault;
				    // var minmem = result.minmem;
				    // var maxmem = result.maxmem;
				    // var multiplayer = result.multiplayer;
				    // var winheight = result.winheight;
				    // var winwidth = result.winwidth;
				    localStorage.setItem('customtheme', result.customtheme);
				    localStorage.setItem('demomode', result.demomode);
				    localStorage.setItem('firsttime', result.firsttime);
				    localStorage.setItem('gamechat', result.gamechat);
				    localStorage.setItem('javapath', result.javapath);
				    localStorage.setItem('jvmargs', result.jvmargs);
				    localStorage.setItem('lastaccount', result.lastaccount);
				    localStorage.setItem('lastinstance', result.lastinstance);
				    localStorage.setItem('maximizedefault', result.maximizedefault);
				    localStorage.setItem('minmem', result.minmem);
				    localStorage.setItem('maxmem', result.maxmem);
				    localStorage.setItem('multiplayer', result.multiplayer);
				    localStorage.setItem('winheight', result.winheight);
				    localStorage.setItem('winwidth', result.winwidth);
				});
			});
		}
	});
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
	console.log(event)
	console.log(event.data)
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