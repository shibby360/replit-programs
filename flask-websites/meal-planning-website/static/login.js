var userdata = localStorage.getItem('userdata')
var link = $('#gotoprof')
if(userdata != null) {
  var data = JSON.parse(userdata)
  link.attr('href', '/profile/'+data.column)
  link[0].click()
}