#!/usr/bin/env python3.6

from sys import argv

def     main():
    try:
        argv[2] * int(argv[1])
    except:
        print("Error")
        exit(89)
    size = len(argv)
    if (size != 3 or int(argv[1]) <= 0):
        print("Error")
    else:
        print(argv[2] * int(argv[1]))

main()
                            
