#!/usr/bin/python3
i = 0
while i < 26: 
    if i != 4 and i != 16:   
        print('{:c}'. format(i + 97), end='')
    i = i + 1
