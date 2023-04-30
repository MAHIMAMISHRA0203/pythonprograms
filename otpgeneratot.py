import random
print('|*|*|*|*|*|*|**THIS IS A OTP GENERATOR|*|*|*|*|*|*|**')
print('Please enter the number of characters you want in your password 4 or 6:')
n=int(input())
l='abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
if (n==6):
    print('The created otp is:')
    for i in range(6):
        re = random.choices(l)
        otp = ''.join(random.choices(l))
        print(otp, end='')
l1='abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM'
if (n == 4):
    print('The created otp is:')
    for i in range(4):
        re = random.choices(l1)
        otp = ''.join(random.choices(l1))
        print(otp, end='')


