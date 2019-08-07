import sys
if len(sys.argv) < 2:
    sys.exit(1)
with open(sys.argv[1], mode='rb') as f:
    lines = f.read()
    lines = lines.split(b'\x0A')
    line = lines[0]
    for i in range(len(lines)):
      if i + 1 < len(lines):
        nextLine = lines[i + 1]
      print('line %d' % i)
      print(line)
      if i == 4:
        print('line %d is %s' % (i, line.decode('utf-8')))
      elif len(nextLine) >=3 and nextLine[0] == 0x00 and nextLine[1] == 0x00 and nextLine[2] == 0x00:
        print('line %d is %s' % (i, line.decode('utf-32')))
        line = nextLine[3:]
      elif len(nextLine) >= 1 and nextLine[0] == 0x00:
        print('line %d is %s' % (i, line.decode('utf-16')))
        line = nextLine[1:]
      else:
        print('line %d is %s' % (i, line.decode('cp949')))
        line = nextLine



