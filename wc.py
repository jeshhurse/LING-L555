import sys

linecount = 0
tokencount = 0
charactercount = 0
vowelcount = 0
conscount = 0

datainput = sys.stdin.readlines()

for line in datainput:
        linecount = linecount + 1

        for char in line:
                charactercount += 1
                if char == " ":
                        tokencount = tokencount + 1
                if char in 'aeiou':
                        vowelcount = vowelcount + 1
                if char in 'bcdfghjklmnpqrstvwxyz':
                        conscount = conscount + 1

sys.stdout.write(str(linecount)+'\n')
sys.stdout.write(str(tokencount)+'\n')
sys.stdout.write(str(charactercount)+'\n')
sys.stdout.write(str(vowelcount)+'\n')
sys.stdout.write(str(conscount)+'\n')


