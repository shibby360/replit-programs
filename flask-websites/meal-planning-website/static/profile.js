localStorage.setItem('userdata', JSON.stringify(userdata))
if(localStorage.getItem('userquestions')) {
  $('#mealplanframe').show()
  var iframebody = $("#mealplanframe").contents().find("body")
}
class emptySpaceElement extends HTMLElement {
  constructor() {
    super()
  }
  connectedCallback() {
    this.attachShadow({ mode: 'open' })
    var count = Number(this.getAttribute('count'))
    var spacestring = '<div style="display: inline;">'
    for(var i = 0; i < count; i++) {
      spacestring += '&nbsp;'
    }
    this.shadowRoot.innerHTML = spacestring + '</div>'
  }
}
customElements.define('empty-space', emptySpaceElement)