#!/usr/bin/env python3
import sys
import re
import string
import secrets

if len(sys.argv) != 2:
    n = 12
else:
    n = int(sys.argv[1])

# In case it is hard to distinguish lowercase from uppercase, we may
# wish to use only lowercase or only uppercase. For now, I'm using
# both but eliminating as many ambiguous characters from alphabet as
# possible (e.g., "O" vs "0", "I" vs "l").
#alphabet = 'abcdefghijmnpqrstuvwxyz0123456789'
#alphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ0123456789'
alphabet = 'abcdefghijmnpqrstuvwxyzABCDEFGHJLMNPQRSTUVWXYZ0123456789'
password = ''.join(secrets.choice(alphabet) for i in range(n))

password = re.sub(r'(....)', r'\1-', password)
password = re.sub(r'-$', '', password)

print("Password:", password)
