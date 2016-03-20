"""Example of the behavior of module importing"""
from __future__ import print_function
import module_one

def tuxy():
	print("I'm gonna pass.")
	pass

if __name__ == "__main__":
    print("You are in the " + __name__)
else:
    print("I'm being imported from {}".format(__name__))

