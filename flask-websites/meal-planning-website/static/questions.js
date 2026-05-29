var bootstrapStyleEl = function() { 
  return $('head>link#bootstrapstylesheet').clone()
}
var scriptEl = function() { 
  return $('body>script#bootstrapscript').clone()
}
function styleEl() {
  return $('head>link#normalcss').clone()
}
class foodPreferences extends HTMLElement {
  constructor() {
    super()
    this.foodchosen = ''
  }
  connectedCallback() {
    var shadow = this.attachShadow({mode:'open'})
    var selectEl = $('<select></select>')
    var labelEl = $(`<label for="${$(this).text().toLowerCase()}">${$(this).text()}</label>`)
    var opts = $(this).attr('opts').split(',')
    var defaultOptEl = $('<option selected disabled hidden>Select</option>')
    selectEl.append(defaultOptEl)
    for(var opt of opts) {
      var optEl = $(`<option value='${opt}'>${opt}</option>`)
      selectEl.append(optEl)
    }
    selectEl.attr('name', $(this).text().toLowerCase())
    $(shadow).append(bootstrapStyleEl())
    $(shadow).append(styleEl())
    $(shadow).append(labelEl)
    $(shadow).append($('<br>'))
    $(shadow).append(selectEl)
    $(shadow).append(scriptEl())
    $(shadow).append($('<br><br>'))
    var thisser = this
    selectEl.on('change', function(ev) {
      thisser.foodchosen = $(ev.target).val()
    })
  }
}
class basicInputs extends HTMLElement {
  constructor() {
    super()
    this.name = ''
    this.age = 0
    this.gender = ''
  }
  connectedCallback() {
    var shadow = this.attachShadow({mode:'open'})
    var inputs = $(`<label for="nameinput">Name</label>
<br>
<input type="text" name="nameinput" id='nameinput'>
<br><br>
<label for="age">Age</label>
<br>
<input type="number" name="age" id='age' min='1'>
<br><br>
<p class='m-0'>Gender</p>
<input type="radio" name="gender" id="gendermale" value="male">
<label for="gendermale">Male</label>
<br>
<input type="radio" name="gender" id="genderfemale" value="female">
<label for="genderfemale">Female</label>
<br><br>`)
    $(shadow).append(bootstrapStyleEl())
    $(shadow).append(styleEl())
    $(shadow).append(inputs)
    $(shadow).append(scriptEl())
    var thisser = this
    inputs.filter('#nameinput').on('input', function(ev) {
      thisser.name = $(ev.target).val()
    })
    inputs.filter('#age').on('input', function(ev) {
      thisser.age = $(ev.target).val()
    })
    inputs.filter('input[name="gender"]').on('input', function(ev) {
      thisser.gender = $(ev.target).val()
    })
  }
}
customElements.define('food-prefs', foodPreferences)
customElements.define('basic-inputs', basicInputs)
function getvalues(ev) {
  var infodict = {}
  var basicInputsInput = $('#basic-inputs')
  var prefs = ['veggies', 'fruits', 'grains']
  for(var i of prefs) {
    infodict[`${i}pref`] = $(`#${i}`)[0].foodchosen
  }
  /*var otherattrs = ['name', 'age', 'gender']
  for(var j of otherattrs) {
    infodict[j] = basicInputsInput[0][j]
  }*/
  localStorage.setItem('userquestions', JSON.stringify(infodict))
}
$('#seeplan').click(getvalues)