#!/usr/bin/env python3
from __future__ import print_function
import sys

if (sys.version_info > (3, 0)):
    import secrets
    RND = secrets
else:
    import random
    RND = random

import re
import string

if len(sys.argv) != 2:
    n = 16
else:
    n = int(sys.argv[1])

alphabet = 'abcdefghijmnpqrstuvwxyz' + string.digits
password = ''.join(RND.choice(alphabet) for i in range(n))

password = re.sub(r'(....)', r'\1-', password)
password = re.sub(r'-$', '', password)

print("Password:", password)
