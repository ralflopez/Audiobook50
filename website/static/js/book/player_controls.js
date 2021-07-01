const playerTime = document.getElementById('player-time')
const duration = document.getElementById('duration')
const currentTime = document.getElementById('current-time')
let isPlaying = false
let isTimeDragging = false
let player
let active

var tag = document.createElement('script')
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0]
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag)

function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '0',
    width: '0',
    videoId: v_id,
    playerVars: {
      'playsinline': 1
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}


function onPlayerReady(event) {
    // configure range
    playerTime.setAttribute('max', player.getDuration())
    playerTime.disabled = false

    // set duration
    duration.innerText = secondsToHms(player.getDuration())

    document.getElementById('play').addEventListener('click', () => {
      event.target.playVideo()
    })
    document.getElementById('pause').addEventListener('click', () => {
      event.target.pauseVideo()
    })
    document.getElementById('stop').addEventListener('click', () => {
        event.target.stopVideo()
    })

    playerTime.addEventListener('mousedown', () => {
      isTimeDragging = true
    })

    playerTime.addEventListener('mouseup', () => {
      player.seekTo(playerTime.value)
      isTimeDragging = false
    })
}


function onPlayerStateChange(event) {
  if (event.data == YT.PlayerState.PLAYING) {
      isPlaying = true
      window.requestAnimationFrame(getCurrentTime)
  } else if (event.data == YT.PlayerState.UNSTARTED) {
      isPlaying = false
      playerTime.value = 0
      currentTime.innerText = 0
    } else {
      isPlaying = false
  }
}

function getCurrentTime() {
    if (!isPlaying) return

    const t = player.getCurrentTime()
    if (!isTimeDragging) playerTime.value = t
    currentTime.innerText = secondsToHms(t)

    active = document.querySelectorAll(`p[ms="${Math.trunc(t)}"]`)
    if (active.length) {
          const prev = transcriptParentContainer.querySelectorAll('.active')
          if (prev) {
              prev.forEach(t => t.className = '')
          }
          active.forEach(t => t.className = 'active')
    }
    
    window.requestAnimationFrame(getCurrentTime)
}

//https://www.codegrepper.com/code-examples/javascript/convert+seconds+to+hours+minutes+seconds+javascript
function secondsToHms(d) {
  d = Number(d);
  var h = Math.floor(d / 3600);
  var m = Math.floor(d % 3600 / 60);
  var s = Math.floor(d % 3600 % 60);

  var hDisplay = h > 0 ? `${padLeadingZeros(h, 2)}:` : "";
  var mDisplay = m > 0 ? `${padLeadingZeros(m, 2)}:` : "00:";
  var sDisplay = s > 0 ? `${padLeadingZeros(s, 2)}` : "00";
  return hDisplay + mDisplay + sDisplay; 
}

// https://www.codegrepper.com/code-examples/javascript/javascript+add+leading+zeros
function padLeadingZeros(num, size) {
  var s = num+"";
  while (s.length < size) s = "0" + s;
  return s;
}