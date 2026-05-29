var alltds = $('tbody > tr > td')
var recipes = JSON.parse($('#recipes').text())
function information(ev) {
  var text = $(ev.target).text()
  $('#recipe').html(recipes[text].replaceAll('\n', '<br>'))
}
alltds.click(information)
var infodict = JSON.parse(localStorage.getItem('userquestions'))
for(var i of Object.keys(infodict)) {
  window[i] = infodict[i]
}
$('.bft.wed').text(`${fruitspref} smoothie`)
if(veggiespref === 'Broccoli' || veggiespref === 'Spinach') {
  $('.lch.wed').text(`Pizza with ${veggiespref}`)
}
$('.sun.dnr').text(`${veggiespref} soup`)
$('.sat.lch').text(`${veggiespref} soup`)
var query = new URLSearchParams(location.search)
if(query.get('iframe') === 'yes') {
  $('body *:not(table, table *, #recipediv, #recipediv *)').hide()
  $('body').css('background', 'none')
  $('body').removeClass('m-2')
  $('body').addClass('m-0')
}