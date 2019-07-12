#!/usr/bin/env python3.6

def main():
    try:
        while 1:
            print(eval(input("bistro>")))
    except SyntaxError:
        print("Syntax error")
    except KeyboardInterrupt:
        print("Ctrl + C")
        exit()
    except Exception as err:
        print(err)

main()