document.addEventListener('keyup', function(key) {
  if(key.key === 'Enter') {
    goo()
  }
})
function goo() {
  localStorage.setItem('char', $('#char').val())
  localStorage.setItem('name', $('#name').val())
  window.location = '/start'
}