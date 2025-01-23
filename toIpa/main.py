ogstring = input('String?: ').lower()
string = ogstring
done = False
f = open('exceptions.txt').read()
g = open('toipa.txt').read()
if string in f.splitlines():
  ind = list(f.splitlines()).index(string)
  print(g.splitlines()[ind])
  done = True
norms = {
  'a':'æ',
  'b':'b',
  'c':'k',
  'd':'d',
  'e':'ɛ',
  'f':'f',
  'g':'g',
  'h':'h',
  'i':'ɪ',
  'j':'dʒ',
  'k':'k',
  'l':'l',
  'm':'m',
  'n':'n',
  'o':'ɔ',
  'p':'p',
  'q':'k',
  'r':'ɹ',
  's':'s',
  't':'t',
  'u':'ə',
  'v':'v',
  'w':'w',
  'x':'ks',
  'y':'j',
  'z':'z'
}
combos = {
  'tion':'∫ən',
  'sh':'∫',
  'tch':'t∫',
  'ch':'t∫',
  'th':'θ',
  'zh':'ʒ',
  'dj':'dʒ',
  'dge':'dʒ',
  'ck':'k',
  'aigh':'áɪ',
  'igh':'áɪ',
  'oo':'ú',
  'ai':'éɪ',
  'ay':'éɪ',
  'oi':'óɪ',
  'oy':'óɪ',
  'ei':'í',
  'ea':'í',
  'ce':'sɛ',
  'ci':'sɪ',
  'cy':'si',
  'er':'ɚ',
  'ir':'ɚ',
  'ur':'ɚ',
  'ng':'ŋ',
  'nk':'ŋk',
  'qu':'kw',
  'wh':'w',
  'ar':'ár',
}
longvowels = {
  'a':'éɪ',
  'e':'í',
  'i':'áɪ',
  'o':'əʊ',
  'u':'ʝú'
}
variants = {
  'ú':'u',
  'é':'e',
  'á':'a',
  'ó':'o',
  'í':'i',
  'ʝ':'j',
}
enders = {
  'a':'ə',
  'e':'',
  'i':'áɪ',
  'o':'əʊ',
  'u':'ʝú',
  'y':'í'
}
if not done:
  string = list(string)
  import re
  import itertools
  regex = r"[aeiou]\w?e"
  matches = re.finditer(regex, ''.join(string), re.MULTILINE)
  for i in matches:
    long = longvowels[i.group()[0]]
    long1 = long[0]
    if len(long) == 2:
      long2 = long[1]
    else:
      long2 = ''
    if len(i.group()) == 3:
      conso = i.group()[1]
    else:
      conso = ''
    if i.span()[1]-1 == len(ogstring)-1:
      thee = ''
    else:
      thee = 'e'
    string[i.span()[0]:i.span()[1]] = [long1, long2, conso, thee]
  
  string = ''.join(string) 
  for i in combos:
    string = string.replace(i, combos[i])
  string = list(string)
  
  for i in range(len(string)):
    if len(string) == 1 or (i == len(string)-1 and string[-1] in ['a','e','i','o','u', 'y']):
      long = enders[string[i]]
      long1 = long[0]
      if len(long) == 2:
        long2 = long[1]
      else:
        long2 = ''
      string[i] = long1
      string.insert(i+1, long2)
    else:
      if string[i] in norms:
        string[i] = norms[string[i]]
  
  for i in range(len(string)):
    if string[i] in variants:
      string[i] = variants[string[i]]
      
  string = ''.join(string)
  string = ''.join(i for i, _ in itertools.groupby(string))
  
  print(string)