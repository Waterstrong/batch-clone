from subprocess import call
from os import path, makedirs
from sys import argv, exit
input_file='homework.txt'

if len(argv) == 2:
    input_file = argv[1]

if not path.isfile(input_file):
    exit('file <{}> not exists\n You can specify input file>$ python batch-clone.py input.txt'.format(input_file))

repository = './{}/'.format(path.splitext(input_file)[0])

if not path.isdir(repository):
    makedirs(repository)

file = open(input_file, 'r')
line_number = 0
for line in file:
    line = line.strip('\n')
    if line:
        line_number += 1
        print ('==========Processing clone/pull project {}: {}=========='.format(line_number, line))
        target_folder = '{}+{}'.format(path.basename(path.dirname(line)), path.splitext(path.basename(line))[0])
        target_path = '{}/{}'.format(repository, target_folder)
        call(['git', 'pull', '-r'], cwd=target_path) if path.isdir(target_path) else call(['git', 'clone', line, target_folder], cwd=repository)
        print

print 'Totally processed {} projects'.format(line_number)
file.close()
