import sys

def format(file_name, separator='\n'):
  if file_name[-4:] != ".txt":
    print("Input file should be of .txt format!")
    return
  with open(file_name, 'r') as f:
    parts = file_name.split('.')
    new_file_name = parts[0] + '_formatted.' + parts[1]
    with open(new_file_name, 'w') as n:
      n.write('|'.join(f.read().split(separator)))

if (len(sys.argv) == 2):
  format(sys.argv[1])
elif (len(sys.argv) == 3):
  format(sys.argv[1], sys.argv[2])
else:
  print('usage: [file-name] [optional: separator]')