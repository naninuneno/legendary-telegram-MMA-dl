(function() {
  
  if (!phantom.args[0]) {
    console.log("No url provided!");
    slimer.exit()
    return;
  }
  
  // "http://alwaysmma.blogspot.co.uk/2017/06/jose-aldo-vs-max-holloway-ufc-212.html";
  var url = phantom.args[0];
  var page = require('webpage').create();
  var lastUrl;

  console.log(phantom.args[0]);

  // monitoring network responses
  page.onResourceReceived = function(response) {
    var url = response['url'];
    if (url.indexOf("hls-vod") !== -1 && url.indexOf("m3u8") !== -1) {
      lastUrl = url;
    }
  };
  page.open(url);

  setTimeout(function () {
    console.log(lastUrl);
    slimer.exit(0);
  }, 10000);
  
}());