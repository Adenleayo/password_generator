# generating a password generator
import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numbers = '0123456789'
symbols = '!@#$%^&*()_.'

string = lower_case + upper_case + Numbers + symbols

#length of the password

length = int(input('enter the length of your password: '))

ans = ''.join(random.sample(string,length))

print(f'your password is {ans} ')
