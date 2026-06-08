import sys

"""
#extra argument not taken care of
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")"""

"""
#IndexError is too few so better to terminate by exit
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])"""

# program working fine without explicit exception handling
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


"""
#slicing shown for more than one argument to be given
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)"""
