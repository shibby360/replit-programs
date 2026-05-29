function logOut() {
  localStorage.removeItem('userdata')
  window.location = '/'
}
var page = location.href.replace('https://meal-planning-app.shivankchhaya.repl.co/', '')
if(page == 'login' || page == 'signup' || page == '') {
  $('.logoutbtn').hide()  
}