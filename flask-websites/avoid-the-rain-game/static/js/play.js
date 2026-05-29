function getCSSVar(x) {
  return getComputedStyle(document.documentElement).getPropertyValue('--' + x)
}
function setCSSVar(x, val) {
  return document.documentElement.style.setProperty(x, val)
}
function remPx(x) {
  return Number(x.replace('px', ''))
}
Array.from($('#speedbox > div')).forEach((el) => {
  for(var i = 10; i >= Number(el.id); i--) {
    $(el).addClass('s' + i)
  }
})
var overlaps = (function () {
    function getPositions( elem ) {
        var pos, width, height;
        pos = $( elem ).position();
        width = $( elem ).width();
        height = $( elem ).height();
        return [ [ pos.left, pos.left + width ], [ pos.top, pos.top + height ] ];
    }

    function comparePositions( p1, p2 ) {
        var r1, r2;
        r1 = p1[0] < p2[0] ? p1 : p2;
        r2 = p1[0] < p2[0] ? p2 : p1;
        return r1[1] > r2[0] || r1[0] === r2[0];
    }

    return function ( a, b ) {
        var pos1 = getPositions( a ),
            pos2 = getPositions( b );
        return comparePositions( pos1[0], pos2[0] ) && comparePositions( pos1[1], pos2[1] );
    };
})();
var gamecontainer = $('#gamecontainer')
var rainintensity = 1
var time = 120
$('#timebox').text(Math.floor(time / 60) + ':' + (time%60<10?'0':'') + (time % 60))
setCSSVar('--rainintensity', (rainintensity + 5) + 'px')
var objects = []
var maxobjs = 40
var objs = 0
function Obstacle(pos) {
  this.el = $('<div class="obstacle rock" style="width: 5%; height: 10%; background: grey;">')
  this.el.css('left', pos)
  objects.push(this)
  gamecontainer.append(this.el)
}
function Tree(pos) {
  this.el = $('<div class="tree">')
  this.el.html(`<div class="treetop"><svg style="
  width: 100%;
  height: 100%;
" viewBox="0 0 100 100" preserveAspectRatio="none">
    <path style="d: path('M60,100 A10,10 0 0,1 21,42 A10,10 0 0,1 43,36 A10,10 0 0,1 63,57 A10,10 0 0,1 89,81 A10,10 0 0,1 89,100 z');fill: green;stroke: green;"></path>
  </svg></div>
<div class="treebottom">
  <svg style="
  width: 100%;
  height: 100%;
" viewBox="0 0 100 100" preserveAspectRatio="none">
    <polyline points="0,0 15,50 10,100" style="
  fill: none;
  stroke: black;
"></polyline>
  <polyline points="20,0 35,50 40,100" style="
  fill: none;
  stroke: black;
"></polyline><polyline points="40,0 55,50 60,100" style="
  fill: none;
  stroke: black;
"></polyline><polyline points="100,0 80,50 75,100" style="
  fill: none;
  stroke: black;
"></polyline></svg>
</div>`)
  this.el.css('left', pos)
  objects.push(this)
  gamecontainer.append(this.el)
}
function Ender(pos) {
  this.el = $('<div class="endblock">')
  this.el.css('left', pos)
  objects.push(this)
  gamecontainer.append(this.el)
}
function Player() {
  this.speed = 1
  this.el = $('#player')
  this.health = 100
  this.update = function() {
    $('#healthbar').css('width', this.health + '%')
  }
  this.isUnderTree = function() {
    var trees = objects.filter((x) => {
      return x.constructor.name == 'Tree'
    })
    var under = false
    trees.forEach((tree) => {
      if(overlaps(this.el[0], tree.el[0])) {
        under = true
      }
    })
    return under
  }
  this.hitEnd = function() {
    var enders = objects.filter((x) => {
      return x.constructor.name == 'Ender'
    })
    enders.forEach((ender1) => {
      if(overlaps(this.el[0], ender1.el[0])) {
        stopall()
      }
    })
  }
  this.checkHits = function() {
    this.hitEnd()
  }
  this.jump = function() {
    var passedMillis = 0
    var self = this
    var upInterval = setInterval(function() {
      if(passedMillis > -25*self.speed+275) {
        clearInterval(upInterval)
        passedMillis = 0
        var downInterval = setInterval(function() {
          self.el.css('top', (40/(-25*self.speed+275) * passedMillis + 45) + '%')
          passedMillis += 1
          if(passedMillis > -25*self.speed+275) {
            clearInterval(downInterval)
          }
        }, 1)
      }
      self.el.css('top', (-40/(-25*self.speed+275) * passedMillis + 65) + '%')
      passedMillis += 1
    }, 1)
  }
}
var player = new Player()
function updateobjs() {
  for(var i in objects) {
    j = objects[i]
    j.el.css('left', j.el[0].offsetLeft - (5*player.speed) + 'px')
    if(j.el[0].offsetLeft+j.el[0].offsetWidth < 0) {
      objects.splice(i, 1)
      j.el.remove()
      if(objects.at(-1).constructor.name == 'Ender') {
        continue
      }
      var w = ['Tree', 'Obstacle'][Math.round(Math.random())]
      var o = new window[w](objSpawnPos + 'px')
      window['objSpawnPos'] = o.el[0].offsetLeft + o.el[0].offsetWidth + 50
      objs += 1
      if(objs >= maxobjs) {
        window['ender'] = new Ender(objSpawnPos + 'px')
      }
    }
  }
}
var raincap = 5
function updaterain() {
  for(var i of Array.from($('.raining'))) {
    var newtop = i.offsetTop + 2
    if(newtop >= gamecontainer[0].offsetHeight) {
      newtop = 0
    }
    i.style.top = newtop + 'px'
  }
  if(rainintensity > raincap && !player.isUnderTree()) {
    player.health -= rainintensity/100
    player.update()
    if(player.health <= 0) {
      stopall()
    }
  }
}
function changeRain() {
  window['rainintensity'] = Math.ceil(Math.random() * 10)
  setCSSVar('--rainintensity', rainintensity + 5 + 'px')
  $('#rainintensebox').html('Rain intensity: ' + rainintensity + '<span class="rainwarn">⚠️</span>')
  if(rainintensity > raincap) {
    $('.rainwarn').addClass('rainwarnflash')
    $('.raining').css('opacity', '1')
  } else {
    $('.rainwarn').removeClass('rainwarnflash')
    $('.raining').css('opacity', '0.5')
  }
  clearInterval(rainFallInterval)
  window['rainFallInterval'] = setInterval(function() {
    updaterain()
  }, -5 * rainintensity + 55)
}
var cn = 1
for(var i = 0; i < gamecontainer[0].offsetHeight / (rainintensity + 5); i += 3) {
  var div = $(`<div class="rain${(cn % 2) + 1} raining">`)
  div.css('width', '100%').css('top', (i * (rainintensity + 5)) + 'px')
  gamecontainer.append(div)
  cn += 1
}
var rainFallInterval = setInterval(function() {
  updaterain()
}, -5 * rainintensity + 55)
var rainIncInterval = setInterval(function() {
  changeRain()
}, 3000)
var objSpawnPos = gamecontainer[0].offsetWidth
for(var i = 0; i < 10; i++) {
  var w = ['Tree', 'Obstacle'][Math.round(Math.random())]
  var o = new window[w](objSpawnPos + 'px')
  objSpawnPos = o.el[0].offsetLeft + o.el[0].offsetWidth + 50
}
objs += 10
var runInterval = setInterval(function() {
  updateobjs()
  player.checkHits()
}, 100)
function stoprain() {
  clearInterval(rainIncInterval)
  clearInterval(rainFallInterval)
}
function stopall() {
  stoprain()
  clearInterval(runInterval)
  clearInterval(timerInterval)
}
$('#speedbox > button').on('click', function(ev) {
  if(ev.target.id == 'incspeed') {
    player.speed += 1
    if(player.speed > 10) {
      player.speed = 10
    }
  } else if(ev.target.id == 'decspeed') {
    player.speed -= 1
    if(player.speed < 0) {
      player.speed = 0
    }
  } else if(ev.target.id == 'stopspd') {
    player.speed = 0
  }
  $('#speedbox > div').css('background', 'linear-gradient(0deg, #c5c5c5, transparent)')
  $('.s' + player.speed).css('background', 'linear-gradient(0deg, black, black, gray)')
  $('#speedbox > *').css('border', `3px rgba(255,0,0,${player.speed/10}) solid`)
})
$(document).on('keydown', function(ev) {
  if(ev.key == 'ArrowRight' || ev.key == 'd') {
    $('#incspeed').click()
  } else if(ev.key == 'ArrowLeft' || ev.key == 'a') {
    $('#decspeed').click()
  } else if(ev.key == ' ' || ev.key == 's' || ev.key == 'ArrowDown') {
    $('#stopspd').click()
  } else if(ev.key == ' ' || ev.key == 'ArrowUp' || ev.key == 'w') {
    player.jump()
  }
})
var timerInterval = setInterval(function() {
  time -= 1
  $('#timebox').text(Math.floor(time / 60) + ':' + (time%60<10?'0':'') + (time % 60))
  if(time === 0) {
    stopall()
  }
}, 1000)