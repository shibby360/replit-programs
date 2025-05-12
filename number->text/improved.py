def textValue(num):
  strn = "{:,}".format(num).split(',')
  end = ''
  cnt = len(strn)
  # ditn = {0:'', 1:'', 2:'', 3:'', 4:'thousand', 5:'ten thousand', 6:'hundred thousand', 7:'million', 8:'ten million', 9:'hundred million', 10:'billion', 11:'ten billion', 12:'hundred billion', 13:'trillion', 14:'ten trillion', 15:'hundred trillion'}
  ditn = {1:'', 2:'thousand', 3:'million', 4:'billion', 5:'trillion', 6:'quadrillion'}
  nmtotxt = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
  cntby10 = {0:'', 1:'ten', 2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
  teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
  cnt = len(strn)
  for i in strn:
    if len(i) == 1:
      end += nmtotxt[int(i)] + ' '
    elif len(i) == 2:
      if i[0] == '1':
        end += teens[int(i)]
      else:
        end += cntby10[int(i[0])] + '-' + nmtotxt[int(i[1])]
      end += ' '
    elif len(i) == 3:
      end += nmtotxt[int(i[0])] + ' hundred '
      if i[1] == '1':
        end += teens[int(i[1:])]
      else:
        end += cntby10[int(i[1])] + '-' + nmtotxt[int(i[2])]
      end += ' '
    end += ditn[cnt] + ' '
    cnt -= 1
  return end.replace(' - ', '').replace('- ', '')
def textValueFloat(num):
  intt = str(num).split('.')[0]
  flo = str(num).split('.')[1]
  ths = {1:'tenths', 2:'hundredths', 3:'thousandths', 4:'ten thousandths', 5:'hundred thousandths', 6:'millionths', 7:'ten millionths', 8:'hundred millionths', 9:'billionths', 10:'ten billionths', 11:'hundred billionths', 12:'trillionths', 13:'ten trillionths', 14:'hundred trillionths', 15:'quadrillionths', 16:'ten quadrillionths', 17:'hundred quadrillionths'}
  end = textValue(int(intt)) + 'and ' + textValue(int(flo)) + ths[len(flo)]
  return end.replace('  ', ' ')