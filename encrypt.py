#!/usr/bin/python3
import bcrypt
import sys

# Get the password from the command line
password = sys.argv[1]

# Convert the password to bytes
bytes = password.encode('utf-8')

# Generate the salt
salt = bcrypt.gensalt()

# Compute the password hash
hash = bcrypt.hashpw(bytes, salt)

# Print password to stdout
print(hash)
