var char = localStorage.getItem('char')
var name = localStorage.getItem('name')
localStorage.removeItem('char')
localStorage.removeItem('name')
if(char === null || name === null) {
  window.location = '/'
}
var suckit = io();
var sid
var charobj
var maxhealth = 1000
var health = 1000
var turn
suckit.emit('werein', {'char':char, 'name':name});
suckit.on('usersid', (data) => {
  sid = data.sid
  $('#n').text('Name: ' + name)
  fetch('/getchar/'+sid).then((r) => {
    r.json().then((j) => {
      charobj = j.char
      $('#he').click(attkr(charobj.specialty, 'red', 'hellblast'))
    })
  })
})
function isDead() {
  return health <= 0
}
function displayStats() {
  $('#h').text('Health: ' + health.toString())
  if(typeof turn === 'boolean') { $('#t').text(turn ? 'Your turn' : 'Opponent\'s turn') }
}
displayStats()
$('#c').text('Your character: ' + char)
function attkr(mode, cColor='white', event='anatk') {
  return function() { 
    if(turn && !isDead()) {
      $('#c').css('color', cColor)
      suckit.emit(event, {sid:sid, atk:charobj, mode:mode})
    } else if(turn === undefined) {
      $('#an').css('color', 'blue')
      setTimeout(function() {
        $('#an').css('color', 'black')
      }, 1000)
    }
  }
}
$('#ap').click(attkr('punch'))
$('#ak').click(attkr('kick'))
/**hellblast button bind is in getuser */
$('#s').click(() => {
  if(turn && !isDead()) {
    $('#sd').show()
  }
})
function talk() {
  var selects = $('#so').children()
  var dandds = {}
  for(var i = 0; i < selects.length; i++) {
    dandds[selects[i].value] = selects[i].classList[0]
  }
  suckit.emit('speech', {dat:$('#so').val(), d:dandds[$('#so').val()]})
  $('#sd').hide()
}
suckit.on('levv', (data) => {
  window.location = '/end'
})
suckit.emit('Join', {sid:sid})
suckit.on('oppsid', (data) => {
  if(data !== 'No opponent yet') {
    fetch('/getchar/'+data).then(function(r) {
      r.json().then(function(j) {
        if(data !== sid) {
          $('#an').text('Opponent: ' + j.name)
        }
      })
    })
  } else {
    $('#an').text(data)
  }
})
suckit.on('whoturn', (data) => {
  if(data === sid) {
    turn = true
  } else {
    turn = false
  }
  displayStats()
})
suckit.on('atk', (data) => {
  if(data.sid === sid) {
  } else {
    health -= data.obj[data.mode]
    if(isDead()) {
      showNotification('Death', 'You died :(', function() {
        window.parent.focus()
        window.location = '/end'
      })
      health = 0
      window.location = '/end'
    } else {
      showNotification('Attack', 'You took ' + (data.obj[data.mode]))
    }
  }
  turn = turn ? false : true
  displayStats()
})
suckit.on('helll', (data) => {
  if(data.sid === sid) {
  } else {
    health -= data.obj.hellblast.damage+data.obj[data.mode]
    if(isDead()) {
      showNotification('Death', 'You died :(', function() {
        window.parent.focus()
        window.location = '/end'
      })
      health = 0
    } else {
      showNotification('Hellblast', 'You took ' + (data.obj.hellblast.damage+data.obj[data.mode]))
    }
  }
  turn = turn ? false : true
  displayStats()
})
suckit.on('atalk', (data) => {
  if(data.sid === sid) {
    
  } else {
    showNotification('Opponent talked', $('#an').text().replace('Opponent: ', '').replace(/^\w/, (c) => c.toUpperCase()) + ' said ' + data.dialog)
  }
  turn = turn ? false : true
  displayStats()
})