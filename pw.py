#! python 3
#pw.py - An insecure password locker program.

PASSWORDS ={'email':'MMihosifwdkfns25193',
            'facebook': '83293472%(^*(^(hsfjskd',
            'blog': 'kabfdkjfk;dfjMMMM',
            'luggage': '21894'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account name '+ account)

