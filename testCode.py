
import os
import sys


def func():
    print('Dead')


def calc_ms(h=1, m=1, s=1, ms=1): return 'Miliseconds: ' + \
    str((((60*h)*60)*1000)+((m*60)*1000)+(s*1000) + ms)


def calc_mns(yr): return 'Months: ' + str(yr*12)

#print(calc_ms())
#print(calc_ms(3, 16, 20, 375))


#print(calc_mns(2))
name = input('What is you name? ')


def capStr(s): return '{}{}'.format(s[0].upper(), s[1:].lower())


print('You typed: '+name)
print('Wellcome {}! Glad you can make it.'.format(capStr(name)))
