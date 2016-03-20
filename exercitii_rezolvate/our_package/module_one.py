'''This is a module implementation part of the package.'''
from __future__ import print_function

def pinguinescu(magicno=42):
    print("Magic " + str(magicno))

def main():
    print("You are in the {0}.".format(__name__))

if __name__ == "__main__": 
    main()
else:
        print("I'm being imported from {}".format(__name__))

