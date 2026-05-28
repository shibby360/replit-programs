f = open('output.txt')
g = f.readlines()
count = 0
while count < 11:
  print(g[count], end='')
  count += 1
f.close()

f = open('output.txt')
g = f.readlines()
print('\x1b[0;35m' + g[11], end='')
f.close()

f = open('output.txt')
h = f.readlines()
counter = 12
while counter < len(h):
  print('\x1b[0;31m' + h[counter], end='')
  counter += 1
f.close()


print('\n\n\x1b[0;0mOutput of hack syntax. Look at main.hack for code.')