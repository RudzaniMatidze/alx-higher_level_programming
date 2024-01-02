#!/usr/bin/python3
num = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - num)), end='')
    num = 32 if num == 0 else 0
