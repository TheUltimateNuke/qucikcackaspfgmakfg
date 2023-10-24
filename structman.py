import fileinput
import glob
import sys


# https://www.geeksforgeeks.org/find-index-closing-bracket-given-opening-bracket-expression/#
def getBlocks(string):
  stack = []
  for i, c in enumerate(string):
    if c == '{':
      stack.append(i)
    elif c == '}' and stack:
      start = stack.pop()
      yield (len(stack), string[start + 1:i])


def entry_point():
  print("Starting Structman...")
  allCSFiles = collectCSFiles()

  for filename in allCSFiles:
    print("checking for structs in " + filename +
          " and removing known compiler bugs...")
    i = 0
    struct_name = ''
    for line in fileinput.input(filename, inplace=True):
      if '.002Ector' in line or 'removed decompiler glitch!' in line:
        print('')
        sys.stderr.write(filename + ": Removed compiler bug! Line: " +
                         str(fileinput.filelineno()) + "\n")
        continue
      if 'struct ' in line:
        i += 1
        struct_name = line.split('struct ')[1].split("{")[0].replace('\n', '')
        sys.stderr.write(filename + ": Found struct name! Line: " +
                         str(fileinput.filelineno()) + " Name: " + struct_name +
                         "\n")
      if struct_name.strip() + '(' in line and not ":this()" in line.replace(' ', ''):
        sys.stderr.write(filename + ": Added :this() to struct constructor! Line: " + str(fileinput.filelineno()) + "\n")
        print(line.rstrip() + ":this()")
        continue
      print(line.replace('\n', ''))


def collectCSFiles():
  print("Collecting C# files..")
  allCSFiles = []

  for filename in glob.iglob('./**/*.cs', recursive=True):
    allCSFiles.append(filename)
    print("found C# file: " + filename + "!")
  return allCSFiles
  
entry_point()
