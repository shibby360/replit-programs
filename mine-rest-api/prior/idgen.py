import string
import random
def gen():
  end = ''
  for i in range(random.randint(25, 30)):
    end += random.choice(string.ascii_letters + string.digits)
  return end