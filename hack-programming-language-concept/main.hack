\I am a comment!


getmod math
getmod math take sub
\Importing modules

go {hewo}
\global variable hewo is 'hello world'

new int(five) { 5 }
new int(six) { math.add(five, 1) }
new int(one) { sub(six, five) }
new list(alpha_to_e) {'a', 'b', 'c', 'd', 'e'}
\variable making

go 'This is six'
go {six}
go {alpha_to_e[4]}
\outputs millions of things

\Im gonna make a function!!
take math
new func(series!!argument1!mode!!) {
  if:mode = 'positive' {
    new int(a) { math.add(argument1, 1) }
    new int(b) { math.mult(a, 2) }
    new int(c) { math.add(b, 3) }
    represent c
  }
  else if:mode = 'negative' {
    new int(a) { math.sub(argument1, 1) }
    new int(b) { math.div(a, 2) }
    new int(c) { math.sub(b, 3) }
    represent c
  }
}
new int(de) { series(4, 'positive') }
go {de}
go {series}

\shell comands
take shell
shell.exec('echo Hello world')

\Let's make a dictionary!
new dict(dictionary) { 
  1:'1', 
  2:'2',
  3:'3',
  4:'4',
  5:'5'
}
go {dictionary{5}}

\Time for classes
new class(A_class) {
  new str(name) { 'A_class' }
  new list(letts_in_name) { name.charify() }\returns ['A', '_', 'c', 'l', 'a', 's', 's']
  new int(atr_count) { 3 }
}
new atr(to: A_class, type: str) { 'Floppp' }
go {A_class.atr_count}
go {A_class}

\Multiple objects which are all similar? Here is your answer!
new constructor(You!!name!age`int`!sigfunction!favthings!!) {
  new me.name = name
  new me.age = age
  new me.sigfunction = sigfunction
  new me.favthings = favthings
}
new obj(Shiv) { inst You('Shiv', 11, new func anony() {
  go 'Shdw boiz'
  new str(shdw) { 'Shdw' }
  go 'I am a ' + shdw
}, ['Shadows', 'Darkness', 'Coding', 'Math']) }
Shiv.sigfunction()

\colors
take colors
new str(green) { colors.purple('Eira') }
go {green}

\Errors
\Im scared
new err(ScaredyCatError)
give_err {
  ErrType:ScaredyCatError
  Err:'You are a scaredy cat'
  ErrLocation:Line(86)
}