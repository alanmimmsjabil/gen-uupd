# gen-uupd
This is a Python3 script to enerate a random unique password for a
unit to comply with CA AB1906/SB-327.

You can use this by 
```
./gen-unit-password.py [ n-chars ]
```
If the _n-chars_ parameter is left off the default is 16.

The password is comprised of most of the lowercase alphabetic letters
with a few removed to eliminate ambiguity with digits and the digits
0-9. Each group of four characters is separated by a "-" with the
remainder at the end. This looks best if the number of characters is a
multiple of four.

For example:
```
$ ./gen-unit-password.py 20
Password: dggd-tqy2-cmxm-42ah-e3g1
```
