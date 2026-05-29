import string
import random as r
def gen():
  end = ''
  rnge = r.randint(10, 25)
  for i in range(rnge):
    end += r.choice(string.digits + string.ascii_letters)
  return end