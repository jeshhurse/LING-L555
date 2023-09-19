import sys

linecount = 0
tokencount = 0
charactercount = 0

datainput = sys.stdin.readlines()

for line in datainput:
        linecount += 1

        for char in line:
                charactercount += 1
                if char == " ":
                        tokencount += 1

sys.stdout.write(str(linecount)+'\n')
sys.stdout.write(str(tokencount)+'\n')
sys.stdout.write(str(charactercount)+'\n')

