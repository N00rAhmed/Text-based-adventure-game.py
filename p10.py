score = 0
q = int(input('what is 2x2: '))
if q == 4:
    print('correct answer, two points')
    score = score + 2
else:
    print('incorrect')
q2 = input('What is the capital city of England: ')
if q2 == 'london':
    print('correct, 3 points')
    score = score + 3
else:
    print('incorrect')

name = input('enter your name: ')

file = open('sc.txt', 'a')
e = file.write(str(score) + ',' + name + '\n')

file.close()

display = str(score)
print('Score: ' + display)

print('''   
            __________________
            |                |   
            |  @        @    |
            |       !        |
            |   \_______/    |
            |________________|''')           