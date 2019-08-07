import sys
if len(sys.argv) < 3:
    sys.exit(1)
with open(sys.argv[1], mode='rb') as f, open(sys.argv[2], mode='w') as fo:
    lines = f.read()
    lines = lines.split(b'\x0A')
    line = lines[0]
    for i in range(len(lines)):
      if i + 1 < len(lines):
        nextLine = lines[i + 1]
      #print(line)
      if len(nextLine) >=3 and nextLine[0] == 0x00 and nextLine[1] == 0x00 and nextLine[2] == 0x00:
        fo.write('line %d (utf-32) %s\n' % (i, line.decode('utf-32')))
        line = nextLine[3:]
      elif len(nextLine) >= 1 and nextLine[0] == 0x00:
        fo.write('line %d (utf-16): %s\n' % (i, line.decode('utf-16')))
        line = nextLine[1:]
      else:
        try:
          fo.write('line %d (cp949): %s\n' % (i, line.decode('cp949')))
        except:
          fo.write('line %d (utf-8): %s\n' % (i, line.decode('utf-8')))
        line = nextLine
