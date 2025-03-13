#!/usr/bin/python3

import bcrypt
import sys

from getopt import getopt, GetoptError
from getpass import getpass

def usage():
    print('usage: encrypt [-b | --bytes PASSWORD] [-o | --out FILE]')
    sys.exit(2)
# Get cli argv and exclude file name
argv = sys.argv[1:]

file = ''
password = ''

# Define the getopt parameters
try:
    opts, args = getopt(argv, 'b:o:', ['bytes', 'out'])
except GetoptError:
    usage()

if len(args) > 0:
    print('Command does not accept any arguments')
    usage()
    
for opt, arg in opts:
    match opt:
        case '-b':
            password = arg
        case '-o':
            file = arg

if password == '':
    password = getpass('Enter password:')

# Convert the password to bytes
bytes = password.encode('utf-8')

# Generate the salt
salt = bcrypt.gensalt()

# Compute the password hash
hash = bcrypt.hashpw(bytes, salt)

hstr = hash.decode()
if file == '':
    # Print hashed password to stdout
    print(hstr)
else:
    # Print hashed password to file
    f = open(file, 'w')
    f.write(hstr + '\n')
    f.close()
