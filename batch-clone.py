import subprocess
git_command = ['git', 'clone']
repository = './homework/'
file = open('homework.txt', 'r')
lineNumber = 0
for line in file:
    line = line.strip('\n')
    if line:
        lineNumber += 1
        print ('==========Processing clone project {}: {}=========='.format(lineNumber, line))
        subprocess.call(['git', 'clone', line])
        print

print 'Totally processed {} projects'.format(lineNumber)
file.close()
