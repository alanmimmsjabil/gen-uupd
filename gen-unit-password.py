#!/usr/bin/env python3
import re
import sys
import string
import secrets

if len(sys.argv) != 2:
    n = 16
else:
    n = int(sys.argv[1])

alphabet = 'abcdefghijmnpqrstuvwxyz' + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(n))

password = re.sub(r'(....)', r'\1-', password)
password = re.sub(r'-$', '', password)

print("Password:", password)
