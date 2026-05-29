let permission = Notification.permission;
if(permission === "default"){
  requestAndShowPermission();
}
function showNotification(title, content, onclickr) {
  if(document.visibilityState === 'visible') {
    alert(content)
    return
  }
  if(onclickr === undefined) {
    onclickr = function() {
      window.parent.focus()
    }
  }
  var notification = new Notification(title, {body:content});
  notification.onclick = () => { 
    notification.close();
    onclickr();
  }
}
function requestAndShowPermission() {
  Notification.requestPermission();
}