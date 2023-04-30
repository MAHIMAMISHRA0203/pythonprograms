import random
print('|*|*|*|*|*|*|**THIS IS A PASSWORD GENERATOR|*|*|*|*|*|*|**')
print('Please enter the number of characters you want in your password between 8 and 12:')
n=int(input())
l='abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()1234567890'
if (8<=n<=12):
    print('The created password is:')
    for i in range(n):
        re = random.choices(l)
        password = ''.join(random.choices(l))
        print(password, end='')
else :
    print('please enter within limit 8 and 12')
