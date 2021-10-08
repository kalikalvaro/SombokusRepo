#!/usr/bin/env  python

import time
import sys


i=1
a='string'
b=0.123

while True: 
    print(f"line {i} {a} {b}")
    i+=1
    b+=(b**2)
    time.sleep(1)
    if i>10: sys.exit()
