print("         ****GUESS THE NUMBER GAME****")
import random
a=int(input('enter starting limit:'))
b=int(input('enter ending  limit:'))
t=int(input('enter  number of turns:'))

r=random.randrange(a,b)
print("  'welcome to GUESS THE NUMBER game \n please choose a number between range' ")
for i in range(t):
    n=int(input('please enter a number:'))
    if (n==r):
        print('yay! you have guessed the right number')
        break
    elif(r>n):
        print('too small')
    elif(n>b or n<a):
        print('please entre a number within the range')
    else:
        print('too large')
