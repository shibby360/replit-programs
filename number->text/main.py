def textValue(num):
  if type(num) == int:
    singles = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'} 
    tens = {10:'ten', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    theInTens = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    teens = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    if num > 1_000_000:
      raise ValueError('Number too large.')
    if len(str(num)) == 1:
      toret = singles[num]
    elif len(str(num)) == 2:
      if str(num)[1] == '0':
        toret = tens[num]
      elif num >= 11 and num <= 19:
        toret = teens[num]
      elif num >= 20 and num <= 99:
        toret = theInTens[int(str(num)[0])] + '-' + singles[int(str(num)[1])]
    elif len(str(num)) == 3:
      toret = singles[int(str(num)[0])] + ' hundred '
      if str(num)[1:] != '00':
        numum = int(str(num)[1:]) 
        if len(str(numum)) == 1:
          toret += singles[numum]
        elif len(str(numum)) == 2:
          if str(numum)[1] == '0':
            toret += tens[numum]
          elif numum >= 11 and numum <= 19:
            toret += teens[numum]
          elif numum >= 20 and numum <= 99:
            toret += (theInTens[int(str(numum)[0])] + '-' + singles[int(str(numum)[1])])
    elif len(str(num)) == 4:
      toret = singles[int(str(num)[0])] + ' thousand '
      if str(num)[1:] != '000':
        if len(str(int(str(num)[1:]))) == 2:
          numme = int(str(num)[1:])
          if str(numme)[1] == '0':
            toret += tens[numme]
          elif numme >= 11 and numme <= 19:
            toret += teens[numme]
          elif numme >= 20 and numme <= 99:
            toret += theInTens[int(str(numme)[0])] + '-' + singles[int(str(numme)[1])]
        elif len(str(int(str(num)[1:]))) == 3:
          numme = int(str(num)[1:])
          toret += singles[int(str(numme)[0])] + ' hundred '
          if str(numme)[1:] != '00':
            numum = int(str(numme)[1:])
            if len(str(numum)) == 1:
              toret += singles[numum]
            elif len(str(numum)) == 2:
              if str(numum)[1] == '0':
                toret += tens[numum]
              elif numum >= 11 and numum <= 19:
                toret += teens[numum]
              elif numum >= 20 and numum <= 99:
                toret += (theInTens[int(str(numum)[0])] + '-' + singles[int(str(numum)[1])])
    elif len(str(num)) == 5 or len(str(num)) == 6:
      num2 = int(str(num)[:-3])
      if len(str(num2)) == 2:
        if str(num2)[1] == '0':
          toret = tens[num2] + ' '
        elif num2 >= 11 and num2 <= 19:
          toret = teens[num2] + ' '
        elif num2 >= 20 and num2 <= 99:
          toret = theInTens[int(str(num2)[0])] + '-' + singles[int(str(num2)[1])] + ' '
      elif len(str(num2)) == 3:
        toret = singles[int(str(num2)[0])] + ' hundred '
        if str(num2)[1:] != '00':
          numum = int(str(num2)[1:])
          if len(str(numum)) == 1:
            toret += singles[numum] + ' '
          elif len(str(numum)) == 2:
            if str(numum)[1] == '0':
              toret += tens[numum] + ' '
            elif numum >= 11 and numum <= 19:
              toret += teens[numum] + ' '
            elif numum >= 20 and numum <= 99:
              toret += (theInTens[int(str(numum)[0])] + '-' + singles[int(str(numum)[1])]) + ' '
      num3 = str(num)[-3:]
      num3_ = list(num3)
      num3_.insert(0, '1')
      num3_ = ''.join(num3_)
      num3 = int(num3_)
      toret += 'thousand '
      if str(num3)[1:] != '000':
        if len(str(int(str(num3)[1:]))) == 2:
          numme = int(str(num3)[1:])
          if str(numme)[1] == '0':
            toret += tens[numme]
          elif numme >= 11 and numme <= 19:
            toret += teens[numme]
          elif numme >= 20 and numme <= 99:
            toret += theInTens[int(str(numme)[0])] + '-' + singles[int(str(numme)[1])]
        elif len(str(int(str(num3)[1:]))) == 3:
          numme = int(str(num3)[1:])
          toret += singles[int(str(numme)[0])] + ' hundred '
          if str(numme)[1:] != '00':
            numum = int(str(numme)[1:])
            if len(str(numum)) == 1:
              toret += singles[numum]
            elif len(str(numum)) == 2:
              if str(numum)[1] == '0':
                toret += tens[numum]
              elif numum >= 11 and numum <= 19:
                toret += teens[numum]
              elif numum >= 20 and numum <= 99:
                toret += (theInTens[int(str(numum)[0])] + '-' + singles[int(str(numum)[1])])
    elif len(str(num)) == 7:
      toret = 'one million'
    return toret
  else:
    raise ValueError('Number is not an integer. Cannot convert to text.')
def textValueFloat(float_):
  if type(float_) == float:
    num = int(str(float_).split('.')[0])
    decimal = int(str(float_).split('.')[1])
    decimalths = {1:'tenths', 2:'hundredths', 3:'thousandths', 4:'ten thousandths', 5:'hundred thousandths', 6:'millionths'}
    toret = textValue(num).strip()
    toret += ' and '
    strdecimal = str(decimal)
    strdecimal = strdecimal.rstrip('0')
    decimal = int(strdecimal)
    if len(str(decimal)) in decimalths:
      toret += textValue(decimal) + ' ' + decimalths[len(str(decimal))]
    else:
      raise ValueError('Too many decimal digits.')
    return toret
  else:
    raise ValueError('Number is not float, cannot convert to text.')


import improved
while True:
  numm = input('What number(up to 15 digits & 14 decimal places)?: ')
  numm = numm.replace(', ', '')
  numm = numm.replace(',', '')
  try:
    print('That number is: ' + str(improved.textValue(int(numm))))
  except ValueError:
    print('That number is: ' + str(improved.textValueFloat(float(numm))))